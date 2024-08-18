from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from . import models

def is_librarian(user):
    return  user.UserProfile.role == 'Librarian'

# @user_passes_test(is_librarian)
# def librarian_view(request):
#     return render(request, template_name="relationship_app/librarian_view.html")


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'profiles/librarian_view.html')