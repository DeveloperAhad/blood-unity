from django.urls import path
from .views import dashboard, search_donors, update_blood_group, search_blood_bank

urlpatterns = [
   path('', dashboard, name='index'),
   path('search_donors', search_donors, name='search_donors'),
   path('search_blood_bank', search_blood_bank, name='search_blood_bank'),
   path('update_blood_group', update_blood_group, name='update_blood_group')
]