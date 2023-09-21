from django.urls import path
from .views import index, chat_box_view

urlpatterns = [
    path('', index, name='chatbox'),
    path('<str:room_name>/', chat_box_view, name='chatbox'),
]