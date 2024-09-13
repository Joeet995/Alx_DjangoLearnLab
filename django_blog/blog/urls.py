from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    # Blog post URLs
    path('posts/', PostListView.as_view(), name='post-list'),  # List of posts
    path("post/new/", PostCreateView.as_view(), name='post-create'),  # Create new post
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View post detail
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),  # Edit post
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name='post-delete'),  # Delete post

    
]
