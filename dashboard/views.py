import json

from django.db.models import Q
from django.shortcuts import render, redirect

from authentication.forms import GeneralUserRegisterForm
from authentication.utility import unauthenticated_user
from backend.settings import BASE_DIR
from blood_banks.models import BloodBank
from dashboard.filters import GeneralUserFilter, BloodBankFilter
from dashboard.form.search import SearchForm
from dashboard.forms import BloodGroupUpdateForm
from general_users.models import GeneralUser


@unauthenticated_user
def index(request):
    return render(request, 'dashboard/index.html')


def dashboard(request):
    context = {
        'user': request.user,
        'blood_bank': BloodBank.objects.get(user_id=request.user.id) if request.user.account_type == 'blood_bank' else None,
        'blood_bank_form': BloodGroupUpdateForm(instance= BloodBank.objects.get(user_id=request.user.id)) if request.user.account_type == 'blood_bank' else None,
    }
    return render(request, 'dashboard/dashboard.html', context)


def update_blood_group(request):
    if request.method == 'POST':
        form = BloodGroupUpdateForm(request.POST, instance=BloodBank.objects.get(user_id=request.user.id))
        if form.is_valid():
            form.save()
            return redirect('/dashboard/')
    return redirect('/dashboard/')


def search_donors(request):
    if request.GET.get('blood_group', None) is not None:
        f = GeneralUserFilter(request.GET, queryset=GeneralUser.objects.filter(~Q(user_id=request.user.id)))
    else:
        f = []
    return render(request, 'dashboard/search-donors.html', {'filter': f, 'form': SearchForm()})


def search_blood_bank(request):
    if request.GET.get('division', None) is not None:
        f = BloodBankFilter(request.GET, queryset=BloodBank.objects.filter(~Q(user_id=request.user.id)))
    else:
        f = []
    return render(request, 'dashboard/search-blood-bank.html', {'filter': f, 'form': SearchForm()})
