from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render
from . import models


def is_librarian(user):
    return  user.UserProfile.role == 'Librarian'

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')