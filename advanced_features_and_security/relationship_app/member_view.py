from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render
from . import models


def is_member(user):
    return user.UserProfile.role == 'Member'

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, template_name="relationship_app/member_view.html")