from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100, blank=False)
    # phone_number = models.CharField(max_length=100, blank=False)
