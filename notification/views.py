from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from notification.models import Notification


# Create your views here.
@login_required
def notification_list_api(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    list = []
    for notification in notifications:
        list.append({
            "title": notification.title,
            "content": notification.content,
            "notification_type": notification.notification_type,
            "post_id": notification.post_id,
            "date": notification.created_at.strftime("%b %d %Y %H:%M:%S"),
        })
    return JsonResponse({"notifications": list})