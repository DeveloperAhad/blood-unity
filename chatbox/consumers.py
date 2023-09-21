import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import ChatRoom, Message  # Import your ChatRoom and Message models

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "buyer_seller_chat_room_%s" % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()
        self.send(text_data=json.dumps({"message": 'connected', 'type': 'connect_message'}))

        # Retrieve and send previous messages when a user connects (if applicable)
        self.send_previous_messages()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_content = text_data_json["message"]
        sender = self.scope["user"]  # Assuming you have user authentication in place

        chat_room = self.get_or_create_chat_room(self.room_name)
        message = Message.objects.create(room=chat_room, sender=sender, content=message_content)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message.content}
        )

    def chat_message(self, event):
        message = event["message"]
        self.send(text_data=json.dumps({"message": message, "type": "chat_message"}))

    def connect_message(self, event):
        message = event["message"]
        self.send(text_data=json.dumps({"message": message, 'type': 'connect_message'}))

    def get_or_create_chat_room(self, room_name):
        try:
            chat_room = ChatRoom.objects.get(name=room_name)
        except ChatRoom.DoesNotExist:
            chat_room = ChatRoom.objects.create(name=room_name)
        return chat_room

    def send_previous_messages(self):
        chat_room = self.get_or_create_chat_room(self.room_name)
        messages = Message.objects.filter(room=chat_room).order_by('timestamp')

        for message in messages:
            self.send(text_data=json.dumps({"message": message.content, "type": "chat_message"}))