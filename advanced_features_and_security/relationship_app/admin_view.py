from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render
from . import models

def is_librarian(user):
    return user.UserProfile.role == 'Admin'

@login_required
@user_passes_test(is_librarian)
def admin_view(request):
    return render(request, template_name="relationship_app/admin_view.html")