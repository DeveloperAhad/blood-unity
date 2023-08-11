from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.db import models
user = get_user_model()

# Create your models here.

class GeneralUser(models.Model):
    class BloodGroup(models.TextChoices):
        A_POSITIVE = 'A+', 'A+'
        A_NEGATIVE = 'A-', 'A-'
        B_POSITIVE = 'B+', 'B+'
        B_NEGATIVE = 'B-', 'B-'
        O_POSITIVE = 'O+', 'O+'
        O_NEGATIVE = 'O-', 'O-'
        AB_POSITIVE = 'AB+', 'AB+'
        AB_NEGATIVE = 'AB-', 'AB-'

    class SelectGender(models.TextChoices):
        MALE = "male", _("Male")
        FEMALE = "female", _("Female")
        OTHER = "other", _("Other")

    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    gender = models.CharField(max_length=10, choices=SelectGender.choices, null=True)
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True)
    division = models.ForeignKey('locations.Division', on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey('locations.District', on_delete=models.SET_NULL, null=True)
    upazila = models.ForeignKey('locations.Upazila', on_delete=models.SET_NULL, null=True)
    union = models.ForeignKey('locations.Union', on_delete=models.SET_NULL, null=True)
    blood_group = models.CharField(max_length=3, choices=BloodGroup.choices, null=True)
    user = models.OneToOneField(user, on_delete=models.CASCADE)