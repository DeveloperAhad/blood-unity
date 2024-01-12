from django import forms
from django.contrib.auth import get_user_model

from blood_banks.models import BloodBank
from general_users.models import GeneralUser

Account = get_user_model()


class BloodGroupUpdateForm(forms.ModelForm):
    class Meta:
        model = BloodBank
        fields = (
            'blood_group_a_positive', 'blood_group_a_negative', 'blood_group_b_positive', 'blood_group_b_negative',
            'blood_group_o_positive', 'blood_group_o_negative', 'blood_group_ab_positive', 'blood_group_ab_negative'
        )
        widgets = {
            'blood_group_a_positive': forms.NumberInput(attrs={'class': 'form-control mb-2'}),
            'blood_group_a_negative': forms.NumberInput(attrs={'class': 'form-control mb-2'}),
            'blood_group_b_positive': forms.NumberInput(attrs={'class': 'form-control mb-2'}),
            'blood_group_b_negative': forms.NumberInput(attrs={'class': 'form-control mb-2'}),
            'blood_group_o_positive': forms.NumberInput(attrs={'class': 'form-control mb-2'}),
            'blood_group_o_negative': forms.NumberInput(attrs={'class': 'form-control mb-2'}),
            'blood_group_ab_positive': forms.NumberInput(attrs={'class': 'form-control mb-2'}),
            'blood_group_ab_negative': forms.NumberInput(attrs={'class': 'form-control mb-2'}),
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Account

        # user_first name, last name, phone number, email, address, division, district, upazila, union, blood groups
        fields = ('first_name', 'last_name', 'email')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'email': forms.TextInput(attrs={'class': 'form-control mb-2'}),
        }

        # email update validation check
        def clean_email(self):
            email = self.cleaned_data.get('email')
            if email != self.instance.email:
                if Account.objects.filter(email=email).exists():
                    raise forms.ValidationError("Email already exists")
            return email


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = GeneralUser

        # user_first name, last name, phone number, email, address, division, district, upazila, union, blood groups
        fields = ('address', 'division', 'district', 'upazila', 'union',
                  'blood_group', 'birth_date', 'avatar'
                  )

        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'division': forms.Select(attrs={'class': 'form-control mb-2'}),
            'district': forms.Select(attrs={'class': 'form-control mb-2'}),
            'upazila': forms.Select(attrs={'class': 'form-control mb-2'}),
            'union': forms.Select(attrs={'class': 'form-control mb-2'}),
            'blood_group': forms.Select(attrs={'class': 'form-control mb-2'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control mb-2', 'type': 'date'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control mb-2'}),
        }

        first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control mb-2'}))
        last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control mb-2'}))


class BloodBankProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = BloodBank

        fields = ('address', 'division', 'district', 'upazila', 'union', 'avatar')

        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'division': forms.Select(attrs={'class': 'form-control mb-2'}),
            'district': forms.Select(attrs={'class': 'form-control mb-2'}),
            'upazila': forms.Select(attrs={'class': 'form-control mb-2'}),
            'union': forms.Select(attrs={'class': 'form-control mb-2'}),
            'blood_group': forms.Select(attrs={'class': 'form-control mb-2'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control mb-2', 'type': 'date'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control mb-2'}),
        }
