from django.shortcuts import render, redirect
from general_users.models import GeneralUser


# Create your views here.
def public_profile(request, id):
    try:
        general_users = GeneralUser.objects.get(id=id)
        context = {
            'general_users': general_users
        }
        return render(request, 'general_user/public_profile.html', context)
    except GeneralUser.DoesNotExist:
        return redirect('dashboard')