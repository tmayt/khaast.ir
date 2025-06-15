from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

class Post(models.Model):
    title = models.CharField(max_length=60)
    TOPIC_CHOICES = [
        ('all', 'عمومی'),
    ]
    topic = models.CharField(max_length=3, choices=TOPIC_CHOICES, default='all')
    body = models.TextField(max_length=10000)
    creator = models.ForeignKey('users.Profile', on_delete=models.CASCADE, blank=True, null=True)
    user_ip = models.GenericIPAddressField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
