
from .models import Author, Book, Library, Librarian

Book.objects.filter(author="george Orwell")

Library.objects.get(name="library_name")

Librarian.objects.grt(library="stans")