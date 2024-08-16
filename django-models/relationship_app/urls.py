from django.urls import path
from . import views
from .views import LibraryDetailView, LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('list_books', views.list_books, name='list_books'),
    path('library_detail', LibraryDetailView.as_view(), name='library_detail'),
    path("register", views.register,name="register"),
    path("login", LoginView.as_view(template_name="login.html"),name="login"),
    path("logout", LogoutView.as_view(template_name="logout.html"),name="logout"),
]