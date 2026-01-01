from django.urls import path

from .views import UserLoginView, UserLogOut, UserProfileView, UserRegistrationView, UserProfileEdit


urlpatterns = [
    path('user_login/', UserLoginView.as_view(), name='user-login'),
    path('user_logout/', UserLogOut.as_view(), name='user-logout'),
    path('user_register/', UserRegistrationView.as_view(), name='user-register'),
    path('user_edit/', UserProfileEdit.as_view(), name='user-edit'),

    path('u/<slug:username>/', UserProfileView.as_view(), name='user-profile'),
]
