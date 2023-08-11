from django.urls import path
from .views import get_districts, get_upazilas, get_unions

urlpatterns = [
    path('districts', get_districts, name='get_districts'),
    path('upazilas', get_upazilas, name='get_upazilas'),
    path('unions', get_unions, name='get_unions'),
]