from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from .managers import AccountManager
import random


# Create your models here.
from .utility import phone_or_email_validator

class Account(AbstractUser):
    class AccountType(models.TextChoices):
        USER = "user", _("User")
        BLOOD_BANK = "blood_bank", _("Blood Bank")

    username = None
    email = models.EmailField(_('email address'), unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    account_type = models.CharField(max_length=20, choices=AccountType.choices, default=AccountType.USER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AccountManager()

    def __str__(self):
        return self.email

    @classmethod
    def general_user_register(cls, first_name, last_name, phone_number, password):
        return cls.objects.create(
            first_name=first_name, last_name=last_name, phone_number=phone_number, password=make_password(password)
        )



class OtpRegister(models.Model):
    phone_number = models.CharField(max_length=11, null=True, blank=True, unique=True)
    email = models.EmailField(_('email address'), unique=True, null=True, blank=True)
    otp = models.CharField(max_length=10, null=True, blank=True)
    is_used = models.BooleanField(default=False)
    test = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone_number

    # 6 digit otp generation
    def generate_otp(self):
        otp = random.randint(1000, 9999)
        self.otp = otp
        self.save()
        return otp

    def verify_otp(self, phone_number, otp):
        try:
            if otp := OtpRegister.objects.get(Q(phone_number=phone_number) | Q(email=phone_number) & Q(otp=otp)):
                otp.is_used = True
                otp.save()
                return True
            else:
                return False
        except Exception:
            return False

    @staticmethod
    def otp_send(phone_or_email):
        if phone_or_email_validator(phone_or_email) == 'email':
            otp, created = OtpRegister.objects.get_or_create(email=phone_or_email)
            return otp.generate_otp()
        elif phone_or_email_validator(phone_or_email) == 'phone':
            otp, created = OtpRegister.objects.get_or_create(phone_number=phone_or_email)
            return otp.generate_otp()
        else:
            return False

    def used_otp(self):
        self.is_used = True
        self.save()
