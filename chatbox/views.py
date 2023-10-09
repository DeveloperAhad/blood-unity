import random

from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from chatbox.models import ChatRoom, Message

Account = get_user_model()


# Create your views here.
def index(request):
    all_chat_rooms = ChatRoom.objects.filter(participants=request.user).order_by('-updated_at')
    rooms = [
        {
            'room_name': chat_room.name,
            'person': chat_room.get_person(request.user),
            'user': chat_room.get_person(request.user).bloodbank
            if chat_room.get_person(request.user).account_type == 'blood_bank'
            else None,
            'unread_messages_count': chat_room.unread_messages(request.user),
        }
        for chat_room in all_chat_rooms
        if chat_room.messages.count() > 0
    ]
    context = {
        'all_chat_rooms': rooms,
    }
    return render(request, 'chat/chat-contacts.html', context)


def create_chat_room(request, participant_id):
    # Create a new chat room with the current user and the user_id passed in the URL
    # Redirect to the chat room view
    user = request.user
    if user.id == participant_id:
        return redirect('/chats/')
    participant = Account.objects.get(id=participant_id)

    existing_chat_room = ChatRoom.objects.filter(participants=user).filter(participants=participant)
    if existing_chat_room.exists():
        return redirect('/chats/' + existing_chat_room[0].name + '/')
    else:
        random_id = random.randint(0, 1000000000)
        new_chat_room = ChatRoom.objects.create(name=str(random_id))
        new_chat_room.participants.add(user)
        new_chat_room.participants.add(participant)
        return redirect('/chats/' + new_chat_room.name + '/')


def chat_box_view(request, room_name):
    # Retrieve the chat room and its messages based on the room_name
    try:
        chat_room = ChatRoom.objects.get(name=room_name)
        messages = Message.objects.filter(room=chat_room).order_by('timestamp')
    except ChatRoom.DoesNotExist:
        return redirect('/chats/')

    context = {
        'chat_room': chat_room,
        'messages': messages,
    }
    return render(request, 'chat/index.html', context)
