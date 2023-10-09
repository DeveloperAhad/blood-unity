from django.db import models
from authentication.forms import User


# Create your models here.

class ChatRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    participants = models.ManyToManyField(User, related_name='chat_rooms')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_person(self, user):
        return next(
            (
                participant
                for participant in self.participants.all()
                if participant != user
            ),
            None,
        )

    def unread_messages(self, user):
        return self.messages.filter(is_read=False).exclude(sender=user).count()

    
class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} in {self.room.name}: {self.content}"
