from django.contrib.gis.geos import Point
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

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


def settings(request):
    if request.method == 'POST':
        request.user.bloodbank.generate_token()

    context = {
        "api_key":  request.user.bloodbank.token
    }
    return render(request, 'blood_bank/settings.html', context)


@csrf_exempt
def update_blood_groups(request):
    if request.method == 'POST':
        token = request.headers.get('Authorization')

        if not token:
            return JsonResponse({'message': 'Token not provided'}, status=401)

        try:
            blood_bank = BloodBank.objects.get(token=token)
        except BloodBank.DoesNotExist:
            return JsonResponse({'message': 'Invalid token'}, status=401)

        data = request.POST   # assuming data is sent as form data, adjust accordingly if using JSON

        print(data)
        # Update blood group values
        blood_bank.blood_group_a_positive = data.get('blood_group_a_positive', blood_bank.blood_group_a_positive)
        blood_bank.blood_group_a_negative = data.get('blood_group_a_negative', blood_bank.blood_group_a_negative)
        blood_bank.blood_group_b_positive = data.get('blood_group_b_positive', blood_bank.blood_group_b_positive)
        blood_bank.blood_group_b_negative = data.get('blood_group_b_negative', blood_bank.blood_group_b_negative)
        blood_bank.blood_group_o_positive = data.get('blood_group_o_positive', blood_bank.blood_group_o_positive)
        blood_bank.blood_group_o_negative = data.get('blood_group_o_negative', blood_bank.blood_group_o_negative)
        blood_bank.blood_group_ab_positive = data.get('blood_group_ab_positive', blood_bank.blood_group_ab_positive)
        blood_bank.blood_group_ab_negative = data.get('blood_group_ab_negative', blood_bank.blood_group_ab_negative)

        blood_bank.save()

        return JsonResponse({'message': 'Blood groups updated successfully'})

    return JsonResponse({'message': 'Invalid request method'})