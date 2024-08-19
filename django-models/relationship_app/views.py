from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth import views, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test, login_required

@login_required
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
    template_name = "relationship_app/login.html"

# Logout view
def user_logout(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

def is_admin(user):
    return user.UserProfile.role == 'Admin'

def is_librarian(user):
    return user.UserProfile.role == 'Librarian'

def is_member(user):
    return user.UserProfile.role == 'Member'

#admin View
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, template_name="relationship_app/admin_view.html")

#librarian view
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, template_name="relationship_app/librarian_view.html")

#member view
@user_passes_test(is_member)
def member_view(request):
    return render(request, template_name="relationship_app/member_view.html")