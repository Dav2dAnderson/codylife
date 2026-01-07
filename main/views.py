from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post, Tags, Replies, Articles, Notification
from .forms import PostCreateForm, ReplyCreateForm
# Create your views here.


class HomePageView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = 'homepage.html'
    context_object_name = 'posts'
    ordering = ['-created_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tags.objects.all()
        return context


class PostCreateView(LoginRequiredMixin, generic.CreateView ):
    model = Post
    template_name = "post_related/post-create.html"
    form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("homepage")


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Post
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'post'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def get_success_url(self):
        return reverse_lazy('homepage')


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Post
    template_name = 'post_related/post-edit.html'
    form_class = PostCreateForm
    # fields = ['body', 'image', 'code', 'tags']
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'post'
    
    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
    
    def get_success_url(self):
        return reverse_lazy('homepage')
    

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_related/post-detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reply_form'] = ReplyCreateForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ReplyCreateForm(request.POST)

        if form.is_valid():
            reply = form.save(commit=False)
            reply.post = self.object
            reply.author = request.user
            reply.save()

            if reply.post.author != self.request.user:
                Notification.objects.create(to_user=reply.post.author, body=f"{self.request.user} postingizga javob yozdi.")            
        return redirect('post-detail', slug=self.object.slug)
    

class NotificationsPageView(LoginRequiredMixin, generic.ListView):
    template_name = 'notifications.html'
    model = Notification
    context_object_name = 'notifications'

    def get_queryset(self):
        qs = Notification.objects.filter(to_user=self.request.user).order_by('-created_date')
        qs.update(is_read=True)
        return qs

class ArticlesPageView(generic.ListView):
    template_name = 'articles/articles.html'
    model = Articles
    context_object_name = 'articles'


class ArticleDetailPageView(generic.DetailView):
    template_name = 'articles/article-detail.html'
    model = Articles
    context_object_name = 'article'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'