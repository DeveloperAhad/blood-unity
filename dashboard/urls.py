from django.urls import path
from .views import dashboard, search_donors

urlpatterns = [
   path('', dashboard, name='index'),
   path('search', search_donors, name='search')
]