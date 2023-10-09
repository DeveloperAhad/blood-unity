from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from general_users.models import GeneralUser
from locations.models import Division, District, Upazila, Union
from .models import Account
User = get_user_model()


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name')


class AccountChangeForm(UserChangeForm):
    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name')


class LoginForm(forms.Form):
    phone_number = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        phone_number = cleaned_data.get('phone_number')
        password = cleaned_data.get('password')

        if phone_number is not None and password:
            user = User.objects.filter(phone_number=phone_number).first()
            if user is None or not user.check_password(password):
                raise forms.ValidationError('Invalid email/password combination')
            self.user = user
        return cleaned_data


class GeneralUserRegisterForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    blood_group = forms.ChoiceField(choices=GeneralUser.BloodGroup.choices)
    gender = forms.ChoiceField(choices=GeneralUser.SelectGender.choices)
    email = forms.EmailField(required=False)
    phone_number = forms.CharField(max_length=11, min_length=11)
    division = forms.ModelChoiceField(queryset=Division.objects.all())
    district = forms.ModelChoiceField(queryset=District.objects.all())
    upazila = forms.ModelChoiceField(queryset=Upazila.objects.all())
    union = forms.ModelChoiceField(queryset=Union.objects.all())
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError({'confirm_password': 'Password mismatched'})

        if User.objects.filter(email=cleaned_data.get('email')).exists():
            raise forms.ValidationError({'email': 'Email already exists'})

        if User.objects.filter(phone_number=cleaned_data.get('phone_number')).exists():
            raise forms.ValidationError({'phone_number': 'Phone number already exists'})
        return cleaned_data


class BloodBankRegisterForm(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    division = forms.ModelChoiceField(queryset=Division.objects.all())
    district = forms.ModelChoiceField(queryset=District.objects.all())
    upazila = forms.ModelChoiceField(queryset=Upazila.objects.all())
    union = forms.ModelChoiceField(queryset=Union.objects.all())
    email = forms.EmailField(required=False)
    phone_number = forms.CharField(max_length=11, min_length=11)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError({'confirm_password': 'Password mismatched'})

        if User.objects.filter(email=cleaned_data.get('email')).exists():
            raise forms.ValidationError({'email': 'Email already exists'})

        if User.objects.filter(phone_number=cleaned_data.get('phone_number')).exists():
            raise forms.ValidationError({'phone_number': 'Phone number already exists'})
        return cleaned_data