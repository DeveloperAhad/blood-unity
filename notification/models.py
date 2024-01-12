from django.db import models

# Create your models here.
class Notification(models.Model):
    class NotificationType(models.TextChoices):
        BLOOD_REQUEST = 'blood_request', 'Blood Request'
        BLOOD_DONATION = 'blood_donation', 'Blood Donation'
        NEWS = 'news', 'News'
        BLOOD_BANK = 'blood_bank', 'Blood Bank'

    title = models.CharField(max_length=100)
    content = models.TextField()
    notification_type = models.CharField(max_length=20, choices=NotificationType.choices, default='blood_request')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post_id = models.IntegerField(null=True)
    user = models.ForeignKey('authentication.Account', on_delete=models.CASCADE)


    def __str__(self):
        return self.title


def create_blood_request_notification(user, requester):
    Notification.objects.create(
        title='Blood Request',
        content='You have a new blood request',
        notification_type=Notification.NotificationType.BLOOD_REQUEST,
        user=user
    )