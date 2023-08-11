from django import forms
from general_users.models import GeneralUser
from locations.models import Division


class SearchForm(forms.Form):
    gender = forms.ChoiceField(choices=GeneralUser.SelectGender.choices, required=False)
    blood_group = forms.ChoiceField(choices=GeneralUser.BloodGroup.choices)
    division = forms.ModelChoiceField(queryset=Division.objects.all(), required=False)
    district = forms.ChoiceField(required=False)
    upazila = forms.ChoiceField(required=False)
    union = forms.ChoiceField(required=False)
    

