from django.contrib import admin

from chatbox.models import ChatRoom, Message


# Register your models here.
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('room', 'sender', 'content', 'is_read', 'timestamp')
    search_fields = ('room', 'sender', 'content')
    list_filter = ('is_read', 'timestamp')


admin.site.register(ChatRoom, ChatRoomAdmin)
admin.site.register(Message, MessageAdmin)
