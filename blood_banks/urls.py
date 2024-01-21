from django.urls import path

from blood_banks.views import public_profile, location_set, settings

urlpatterns = [
   path('profle/<str:id>', public_profile, name='blood_bank_public_profile'),
   path('location/set', location_set, name='blood_bank_location_set'),
    path('settings', settings, name='blood_bank_settings'),
]