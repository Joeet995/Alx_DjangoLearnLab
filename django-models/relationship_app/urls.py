from django.urls import path
from .views import register, list_books, LoginView
from .views import LibraryDetailView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('list_books', list_books, name='list_books'),
    path('library_detail', LibraryDetailView.as_view(), name='library_detail'),
    path("register", register,name="register"),
    path("login", LoginView.as_view(),name="login"),
    path("logout", LogoutView.as_view(),name="logout"),
]