from django.contrib.auth import get_user_model
from .models import Notification
Account = get_user_model()


def create_news_create_notification_for_all_users( post_id):
    users = Account.objects.all()
    for user in users:
        Notification.objects.create(
            title='News',
            content='You have a new news',
            notification_type=Notification.NotificationType.NEWS,
            user=user,
            post_id=post_id
        )