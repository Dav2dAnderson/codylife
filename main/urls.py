from django.urls import path

from .views import HomePageView, PostCreateView, PostDeleteView, PostUpdateView, PostDetailView


urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('post-create/', PostCreateView.as_view(), name='post-create'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<slug:slug>/update/', PostUpdateView.as_view(), name='post-edit'),
    path('post/<slug:slug>/detail/', PostDetailView.as_view(), name='post-detail')
]