from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=256, blank=False)
    email = models.EmailField(null=False, unique=True)
    #####
    OTP = models.TextField(default='')
    OTP_generated_datetime = models.DateTimeField(blank=True, null=True)
    OTP_expiration_datetime = models.DateTimeField(blank=True, null=True)
    is_account_verified = models.BooleanField(default=False)
    account_verified_datetime = models.DateTimeField(blank=True, null=True)
    password_reset_OTP = models.TextField(default='')
    password_reset_request = models.BooleanField(default=False)
    password_reset_request_sent_datetime = models.DateTimeField(blank=True, null=True)
    password_reset_request_expiration = models.DateTimeField(blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
