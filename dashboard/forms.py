from blood_banks.models import BloodBank
from django import forms


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
