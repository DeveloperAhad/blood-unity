# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Notification

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        user = self.scope['user']
        if user.is_authenticated:
            await self.join_notification_group(user.id)
            await self.send_notification({"message": "Connected!", "message_type": "connect_message"})

    async def disconnect(self, close_code):
        user = self.scope['user']
        if user.is_authenticated:
            await self.leave_notification_group(user.id)

    async def receive(self, text_data):
        # Handle incoming data (if needed)
        text_data_json = json.loads(text_data)
        message_content = text_data_json["message"]
        message_type = text_data_json["message_type"]

        print(message_content)
        print(message_type)



    async def send_notification(self, event):
        # Send notification to the WebSocket
        await self.send(text_data=json.dumps(event))

    @database_sync_to_async
    def join_notification_group(self, user_id):
        print(f'user_{user_id}_notifications')
        async_to_sync(self.channel_layer.group_add)(
            f"user_{user_id}_notifications", self.channel_name
        )

    @database_sync_to_async
    def leave_notification_group(self, user_id):
        async_to_sync(self.channel_layer.group_discard)(
            f"user_{user_id}_notifications", self.channel_name
        )


@database_sync_to_async
@receiver(post_save, sender=Notification)
def handle_notification(sender, instance, **kwargs):
    group_name = f"user_{instance.user.id}_notifications"
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        group_name, {
            "type": "send_notification",
            "title": instance.title,
            "content": instance.content,
            "notification_type": instance.notification_type,
            "post_id": instance.post_id,
            "date": instance.created_at.strftime("%b %d %Y %H:%M:%S"),
        }
    )
