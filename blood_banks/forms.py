from django import forms


class BloodBankLocationSetForm(forms.Form):
    lat = forms.FloatField()
    lng = forms.FloatField()