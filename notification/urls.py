from django.urls import path
from .views import notification_list_api


urlpatterns = [
   path('', notification_list_api, name='notification_list_api')
]