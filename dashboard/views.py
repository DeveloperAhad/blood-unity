from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.db.models import Q
from django.shortcuts import render, redirect

from authentication.utility import unauthenticated_user
from blood_banks.models import BloodBank
from dashboard.filters import GeneralUserFilter, BloodBankFilter
from dashboard.form.search import SearchForm
from dashboard.forms import BloodGroupUpdateForm, ProfileUpdateForm, UserUpdateForm, BloodBankProfileUpdateForm
from general_users.models import GeneralUser


@unauthenticated_user
def index(request):
    return render(request, 'dashboard/index.html')


def profile_view(request):
    if request.user.account_type == 'blood_bank':
        if request.method == 'POST':
            form1 = BloodBankProfileUpdateForm(request.POST, instance=request.user.bloodbank)
            form2 = UserUpdateForm(request.POST, instance=request.user)
            if form1.is_valid() and form2.is_valid():
                form1.save()
                form2.save()
                return redirect('/dashboard/profile')
            else:
                return render(request, 'dashboard/profile.html', {'form1': form1, 'form2': form2})
        else:
            form1 = BloodBankProfileUpdateForm(instance=request.user.bloodbank)
            form2 = UserUpdateForm(instance=request.user)
            return render(request, 'dashboard/profile.html', {'form1': form1, 'form2': form2, 'blood_bank': request.user.bloodbank})
    else:
        if request.method == 'POST':
            form1 = ProfileUpdateForm(request.POST, instance=request.user.generaluser)
            form2 = UserUpdateForm(request.POST, instance=request.user)
            if form1.is_valid() and form2.is_valid():
                form1.save()
                form2.save()
                return redirect('/dashboard/profile')
            else:
                return render(request, 'dashboard/profile.html', {'form1': form1, 'form2': form2})
        else:
            form1 = ProfileUpdateForm(instance=request.user.generaluser)
            form2 = UserUpdateForm(instance=request.user)
            return render(request, 'dashboard/profile.html', {'form1': form1, 'form2': form2})


def dashboard(request):
    context = {
        'user': request.user,
        'blood_bank': BloodBank.objects.get(
            user_id=request.user.id) if request.user.account_type == 'blood_bank' else None,
        'blood_bank_form': BloodGroupUpdateForm(instance=BloodBank.objects.get(
            user_id=request.user.id)) if request.user.account_type == 'blood_bank' else None,
        'all_blood_bank': BloodBank.objects.all(),
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


def near_by_blood_banks(request):
    lat = request.GET.get('latitude', None)
    lng = request.GET.get('longitude', None)
    if lat is None or lng is None:
        return redirect('/dashboard/')
    target_point = Point(x=float(lng), y=float(lat), srid=4326)
    queryset = BloodBank.objects.filter(location_point__distance_lte=(target_point, Distance(km=10)))
    return render(request, 'dashboard/nearby-blood-bank.html', {'blood_banks': queryset})


def near_by_donors(request):
    lat = request.GET.get('latitude', None)
    lng = request.GET.get('longitude', None)
    if lat is None or lng is None:
        return redirect('dashboard')
    target_point = Point(x=float(lng), y=float(lat), srid=4326)
    queryset = GeneralUser.objects.filter(last_point__distance_lte=(target_point, Distance(km=10)))
    return render(request, 'dashboard/nearby-donors.html', {'donors': queryset})