from django.shortcuts import render, redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views import generic
from django.contrib import messages
from django.db import IntegrityError
from django import forms
from django.urls import reverse_lazy

from .models import CustomUser
from .forms import CustomUserCreationForm, EditProfileForm
# Create your views here.


class UserRegistrationView(View):
    def get(self, request):
        form  = CustomUserCreationForm()
        return render(request, 'auth/registration.html', {'form': form})
    
    def post(self, request):
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome to CodeLify, {user.username}!")
            return redirect('homepage')
        else:
            messages.error(request, "Please correct the errors below.")

        return render(request, 'auth/registration.html', {'form': form})    
        # username = self.request.POST.get('username')
        # email = self.request.POST.get('email')
        # password1 = self.request.POST.get('password1')
        # password2 = self.request.POST.get('password2')

        # if not username or not email or not password1 or not password2:
        #     messages.error(request, 'All fields are required.')
        #     return render(request, 'auth/registration.html')
        
        # if password1 != password2:
        #     messages.error(request, 'Password do not match.')
        #     return render(request, 'auth/registration.html')
        
        # if len(password1) < 8:
        #     messages.error(request, "Password must be at least 8 characters long.")
        #     return render(request, 'auth/registration.html')
        
        # if CustomUser.objects.filter(email=email).exists():
        #     messages.error(request, 'Email already registered.')
        #     return render(request, 'auth/registration.html')

        # try:
        #     user = CustomUser.objects.create_user(
        #         username=username,
        #         email=email,
        #         password=password1
        #     )
        #     login(request, user)
        #     messages.success(request, f"Welcome to CodyLife {username}")
        #     return redirect('homepage')
        # except IntegrityError:
        #     messages.error(request, "An error occurred. Please try again.")
        #     return render(request, 'auth/registration.html')
        

# @method_decorator(csrf_protect, name='dispatch')
class UserLoginView(View):
    def get(self, request):
        return render(request, 'auth/login.html')
    
    def post(self, request):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')    

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            request.session.cycle_key()
            return redirect('user-profile', user.username)
        

class UserLogOut(View):
    def get(self, request):
        return render(request, 'auth/logout.html')
    
    def post(self, request):
        logout(request)
        return redirect('user-login')
    

class UserProfileView(generic.DetailView):
    model = CustomUser
    template_name = 'user-profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    context_object_name = 'profile_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context
    

class UserProfileEdit(generic.UpdateView):
    model = CustomUser
    form_class = EditProfileForm
    template_name = 'edit-profile.html'

    def get_object(self, queryset = None):
        return self.request.user
    
    def get_success_url(self):
        return reverse_lazy('user-profile', kwargs={"username": self.request.user.username})