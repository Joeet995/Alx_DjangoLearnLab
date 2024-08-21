
from .models import Author, Book, Library, Librarian


#List all books in a library.
def list_books(library_name):
    library = Library.objects.get(name=library_name)
    books = Library.books.get(name=library)
    return books

Author.objects.get(name=author_name)
objects.filter(author=author)

#Retrieve the librarian for a library.
def Librarian_for_library(Library_name):
    library = Library.objects.get(name=Library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian