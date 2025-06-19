from django.contrib import admin
from .models import Post, Reply

class PostAdmin(admin.ModelAdmin):
    search_fields = ["title", "creator"]
    list_display = ["title", "topic", "creator", "created"]

admin.site.register(Post, PostAdmin)

class ReplyAdmin(admin.ModelAdmin):
    search_fields = ["post__title", "text", 'pk']
    list_display = ["post", "text", "created"]

admin.site.register(Reply, ReplyAdmin)
