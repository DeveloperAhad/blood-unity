from django.shortcuts import render

from chatbox.models import ChatRoom, Message


# Create your views here.
def index(request):
    return render(request, 'chat/index.html')


def chat_box_view(request, room_name):
    # Retrieve the chat room and its messages based on the room_name
    try:

        all_chat_rooms = ChatRoom.objects.filter(participants=request.user)
        chat_room = ChatRoom.objects.get(name=room_name)
        messages = Message.objects.filter(room=chat_room).order_by('timestamp')
    except ChatRoom.DoesNotExist:
        # Handle the case when the chat room doesn't exist
        chat_room = None
        messages = []

    context = {
        'chat_room': chat_room,
        'messages': messages,
        'all_chat_rooms': all_chat_rooms,
    }
    return render(request, 'chat/index.html')
