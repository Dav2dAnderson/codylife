from django.urls import path
from django.contrib.auth import views as auth_views

from .forms import CustomPasswordChangeForm
from .views import UserLoginView, UserLogOut, UserProfileView, UserRegistrationView, UserProfileEdit, SettingsView, EmailVerifyView


urlpatterns = [
    path('user_login/', UserLoginView.as_view(), name='user-login'),
    path('user_logout/', UserLogOut.as_view(), name='user-logout'),
    path('user_register/', UserRegistrationView.as_view(), name='user-register'),
    path('user_edit/', UserProfileEdit.as_view(), name='user-edit'),

    path('u/<slug:username>/', UserProfileView.as_view(), name='user-profile'),
    path('settings/', SettingsView.as_view(), name='settings'),

    path('password/change/', auth_views.PasswordChangeView.as_view(
        form_class = CustomPasswordChangeForm,
        template_name = 'settings/password_change.html',
        success_url = '/users/password/change/done/'
    ),
    name='password-change'),
    path('password/change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='settings/password_change_done.html'
    ),
    name='password-change-done'),

    path('verify/<uuid:code>/', EmailVerifyView.as_view(), name='email-verify'),
]
