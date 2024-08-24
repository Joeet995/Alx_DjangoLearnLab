from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book, Bookform


# Create your views here.
@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_books(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = Bookform(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = Bookform(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})

from .forms import ExampleForm

def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the form data
            return render(request, 'bookshelf/form_success.html')
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})