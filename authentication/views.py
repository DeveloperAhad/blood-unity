import json

from django.contrib import messages
from django.contrib.auth import login, logout, get_user_model
from django.shortcuts import render, redirect

# Create your views here.
from authentication.forms import LoginForm, GeneralUserRegisterForm, BloodBankRegisterForm
from authentication.utility import unauthenticated_user
from backend.settings import BASE_DIR
from blood_banks.models import BloodBank
from general_users.models import GeneralUser

User = get_user_model()


@unauthenticated_user
def login_view(request):
    context = {
        'form': LoginForm()
    }

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.user
            login(request, user)
            return redirect('/dashboard/')
        context = {
            'form': form
        }
    return render(request, 'auth/login.html', context)


def register_view(request):
    with open(f'{BASE_DIR}/static/jsons/bd-districts.json', 'r') as json_file:
        json_dict = json.load(json_file)

        context = {
            'json_dict': json_dict,
            'form': GeneralUserRegisterForm(),
            'blood_bank_form': BloodBankRegisterForm()
        }
    if request.method == 'POST':

        active_blood_bank_form = False
        form = GeneralUserRegisterForm(request.POST)
        blood_bank_form = BloodBankRegisterForm(request.POST)

        if request.POST.get('form_name', None) == 'blood_bank':
            active_blood_bank_form = True

        if request.POST.get('form_name', None) == 'general_user' and form.is_valid():
            user = User().general_user_register(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password'],
                phone_number=form.cleaned_data['phone_number'],
            )

            GeneralUser.objects.create(
                user=user,
                gender=form.cleaned_data['gender'],
                birth_date=form.cleaned_data['birth_date'],
                blood_group=form.cleaned_data['blood_group'],
                division=form.cleaned_data['division'],
                district=form.cleaned_data['district'],
                upazila=form.cleaned_data['upazila'],
                union=form.cleaned_data['union'],
            )

            messages.success(request, 'Your account has been created successfully!')

        elif request.POST.get('form_name', None) == 'blood_bank' and blood_bank_form.is_valid():
            user = User().blood_bank_register(
                name=blood_bank_form.cleaned_data['name'],
                password=blood_bank_form.cleaned_data['password'],
                phone_number=blood_bank_form.cleaned_data['phone_number'],
            )

            BloodBank.objects.create(
                user=user,
                address=blood_bank_form.cleaned_data['address'],
                division=blood_bank_form.cleaned_data['division'],
                district=blood_bank_form.cleaned_data['district'],
                upazila=blood_bank_form.cleaned_data['upazila'],
                union=blood_bank_form.cleaned_data['union'],
            )
            messages.success(request, 'Your account has been created successfully!')

        else:
            context = {
                'form': form,
                'blood_bank_form': blood_bank_form,
                'active_blood_bank_form': active_blood_bank_form
            }
    return render(request, 'auth/general_user_register.html', context)


def general_user_register_view(request):
    if request.method == 'POST':
        form = GeneralUserRegisterForm(request.POST)
        # if form.is_valid():
        context = {
            'form': form
        }
        return redirect('register', context)


def logout_view(request):
    logout(request)
    return redirect('login')
