from django.shortcuts import render, redirect

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