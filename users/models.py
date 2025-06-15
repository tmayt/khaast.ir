from django.contrib.auth.models import AbstractUser
from django.db import models

class Profile(AbstractUser):
    address = models.TextField(null=True, blank=True)
    last_location = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username
