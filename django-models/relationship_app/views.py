from django.shortcuts import render
from .models import Book

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    context = {'list_books': books}
    return render(request, 'relationship_app/list_books.html', context)

