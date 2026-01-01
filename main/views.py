from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post, Tags
from .forms import PostCreateForm
# Create your views here.


class HomePageView(generic.ListView):
    model = Post
    template_name = 'homepage.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tags.objects.all()
        return context

class PostCreateView(generic.CreateView ):
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
    