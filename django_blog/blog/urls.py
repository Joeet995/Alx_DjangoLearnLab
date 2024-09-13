from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentDeleteView,
    CommentUpdateView,
    TaggedPostListView,
    search_posts,
    PostByTagListView
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
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Edit post
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name='post-delete'),  # Delete post

    # Comment URLs
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add-comment'),  # Add comment
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete-comment'),  # Delete comment
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='update-comment'),  # Update comment

    # Search and Tagging URLs
    path('search/', search_posts, name='search-posts'),  # Search posts  
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'), #post by tag
]

