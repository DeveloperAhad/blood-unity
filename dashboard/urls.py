from django.urls import path, include
from .views import dashboard, search_donors, update_blood_group, search_blood_bank, profile_view, near_by_blood_banks, near_by_donors

urlpatterns = [
   path('', dashboard, name='index'),
   path('search_donors', search_donors, name='search_donors'),
   path('search_blood_bank', search_blood_bank, name='search_blood_bank'),
   path('update_blood_group', update_blood_group, name='update_blood_group'),
   path('profile', profile_view, name='profile'),
   path('portal/', include('portal.urls')),
   path('near_by_blood_banks', near_by_blood_banks, name='near_by_blood_banks'),
   path('near_by_donors', near_by_donors, name='near_by_donors'),
]