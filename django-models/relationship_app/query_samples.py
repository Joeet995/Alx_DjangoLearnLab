from .models import Author, Book, Library, Librarian

Book.objects.filter(author="George Orwell")

Library.objects.all()

Librarian.objects.get(library="stans")