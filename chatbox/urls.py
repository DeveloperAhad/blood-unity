from django.urls import path
from .views import index, chat_box_view, create_chat_room

urlpatterns = [
    path('', index, name='chatbox_index'),
    path('<str:room_name>/', chat_box_view, name='chat_room'),
    path('create_chat/<str:participant_id>/', create_chat_room, name='create_chat_room'),
]