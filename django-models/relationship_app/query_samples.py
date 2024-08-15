
from .models import Author, Book, Library, Librarian

Book.objects.filter(author="george Orwell")

Library.objects.get(name="library_name")
books.all()

Librarian.objects.grt(library="stans")