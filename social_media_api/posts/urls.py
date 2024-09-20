from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, UserFeedView, LikePostView, UnlikePostView
from django.urls import path, include

router = DefaultRouter()
router.register(r'posts', PostViewSet,)
router.register(r'comments', CommentViewSet,)

urlpatterns = [
    path('feed/', UserFeedView.as_view(), name='user-feed'),
    path('<int:pk>/like/', LikePostView.as_view(), name='like_post'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike_post'),
]

urlpatterns += router.urls
