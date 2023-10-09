from django.urls import path
from general_users.views import public_profile

urlpatterns = [
   path('profle/<str:id>', public_profile, name='public_profile'),
]