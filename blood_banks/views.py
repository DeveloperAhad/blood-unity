from django.contrib.gis.geos import Point
from django.shortcuts import render, redirect

from blood_banks.forms import BloodBankLocationSetForm
from blood_banks.models import BloodBank


# Create your views here.
def public_profile(request, id):
    try:
        blood_bank = BloodBank.objects.get(id=id)
        context = {
            'blood_bank': blood_bank
        }
        return render(request, 'blood_bank/public_profile.html', context)
    except BloodBank.DoesNotExist:
        return redirect('dashboard')



def location_set(request):
    form = BloodBankLocationSetForm(request.POST or None)
    if form.is_valid():
        lat = form.cleaned_data.get('lat')
        lng = form.cleaned_data.get('lng')
        request.user.bloodbank.location_point =  Point(float(lng), float(lat))
        request.user.bloodbank.lat = lat
        request.user.bloodbank.lng = lng
        request.user.bloodbank.save()

    return redirect('profile')