import django_filters

from general_users.models import GeneralUser


class GeneralUserFilter(django_filters.FilterSet):
    class Meta:
        model = GeneralUser
        fields = ['gender', 'blood_group', 'division', 'district', 'upazila', 'union']