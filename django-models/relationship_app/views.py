from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth import views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'list_books': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Login")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form":form})

class LoginView(views.LoginView):
    template_name = "login.html"

def is_admin(user):
    return user.is_autheticated and user.UserProfile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, template_name="relationship_app/admin_view.html")

def is_librarian(user):
    return user.is_autheticated and user.UserProfile.role == 'Librarians'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, template_name="relationship_app/librarian_view.html")