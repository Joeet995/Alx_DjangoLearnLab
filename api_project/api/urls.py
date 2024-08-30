from django.urls import path, include
from .views import BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('books', BookViewSet, basename='book')

urlpatterns = router.urls
urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]