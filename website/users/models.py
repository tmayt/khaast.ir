from django.contrib.auth.models import AbstractUser
from django.db import models

class Profile(AbstractUser):
    address = models.TextField(null=True, blank=True)
    last_location = models.CharField(max_length=255, null=True, blank=True)
    BLOOD_CHOICES = [
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),

        ('A+', 'A+'),
        ('A-', 'A-'),

        ('B+', 'B+'),
        ('B-', 'B-'),

        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    blood_group = models.CharField(max_length=3, choices=BLOOD_CHOICES, default='a')
    national_id = models.CharField(max_length=10)

    def __str__(self):
        return self.username
