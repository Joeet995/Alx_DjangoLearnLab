from django.urls import path
from . import views
from .views import LibraryDetailView, LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('list_books', views.list_books, name='list_books'),

#library detail URL
    path('library_detail', LibraryDetailView.as_view(), name='library_detail'),

#user authentications URL
    path("register", views.register,name="register"),
    path("login", LoginView.as_view(template_name="login.html"),name="login"),
    path("logout", LogoutView.as_view(template_name="logout.html"),name="logout"),

#Role-Based Views URL
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),

# Book-related URLs
    path('add_book/add/', views.add_book, name="add_book"),
    path('edit_book/<int:pk>/edit/', views.edit_book, name="edit_book"),
    path('delete_book/<int:pk>/delete/', views.delete_book, name="delete_book"),
]