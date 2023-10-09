import django_filters

from blood_banks.models import BloodBank
from general_users.models import GeneralUser


class GeneralUserFilter(django_filters.FilterSet):
    class Meta:
        model = GeneralUser
        fields = ['gender', 'blood_group', 'division', 'district', 'upazila', 'union']


class BloodBankFilter(django_filters.FilterSet):
    class Meta:
        model = BloodBank
        fields = ['division', 'district', 'upazila', 'union']
