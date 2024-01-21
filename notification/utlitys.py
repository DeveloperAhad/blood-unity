from django.contrib.auth import get_user_model

from blood_banks.models import BloodBank
from general_users.models import GeneralUser
from .models import Notification
Account = get_user_model()


def create_news_create_notification_for_all_users(post_id):
    users = Account.objects.all()
    for user in users:
        Notification.objects.create(
            title='New Community Post',
            content='Stay connected! A fresh community post is up. Check it out for the latest updates, announcements, and discussions.',
            notification_type=Notification.NotificationType.NEWS,
            user=user,
            post_id=post_id
        )

def create_blood_request_notifications(post_id, blood_group, district):
    users = GeneralUser.objects.filter(blood_group=blood_group, district=district)
    for user in users:
        Notification.objects.create(
            title='Urgent: Blood Needed!',
            content='Your local area urgently requires blood donations. Your contribution can save lives.',
            notification_type=Notification.NotificationType.BLOOD_REQUEST,
            user=user.user,
            post_id=post_id
        )

def create_blood_bank_notifications(post_id, blood_group, district):
    users = BloodBank.objects.filter(district=district)
    for user in users:
        Notification.objects.create(
            title='Urgent: Blood Needed!',
            content='Your local area urgently requires blood donations. Your contribution can save lives.',
            notification_type=Notification.NotificationType.BLOOD_BANK,
            user=user.user,
            post_id=post_id
        )