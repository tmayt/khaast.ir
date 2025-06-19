from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

class Reply(models.Model):
    text = models.TextField()
    post = models.ForeignKey('main.Post', on_delete=models.CASCADE, related_name="replies")
    creator = models.ForeignKey('users.Profile', on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    user_ip = models.GenericIPAddressField(blank=True, null=True)

    def __str__(self):
        return self.post

class Post(models.Model):
    title = models.CharField(max_length=60)
    TOPIC_CHOICES = [
        ('a', 'عمومی'),
    ]
    topic = models.CharField(max_length=1, choices=TOPIC_CHOICES, default='a')
    body = models.TextField()
    creator = models.ForeignKey('users.Profile', on_delete=models.CASCADE, blank=True, null=True)
    user_ip = models.GenericIPAddressField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
