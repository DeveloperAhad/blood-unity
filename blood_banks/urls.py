from django.urls import path

from blood_banks.views import public_profile

urlpatterns = [
   path('profle/<str:id>', public_profile, name='blood_bank_public_profile'),
]