import json

from django.shortcuts import render, redirect

from authentication.forms import GeneralUserRegisterForm
from authentication.utility import unauthenticated_user
from backend.settings import BASE_DIR
from dashboard.filters import GeneralUserFilter
from dashboard.form.search import SearchForm
from general_users.models import GeneralUser


@unauthenticated_user
def index(request):
    return render(request, 'dashboard/index.html')


def dashboard(request):

    context = {
        'user': request.user
    }
    return render(request, 'dashboard/dashboard.html', context)

def search_donors(request):

    f = GeneralUserFilter(request.GET, queryset=GeneralUser.objects.all())
    return render(request, 'dashboard/search-donors.html', {'filter': f, 'form': SearchForm()})