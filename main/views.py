from django.shortcuts import render, get_object_or_404
from .models import Post
from users.decorators import login_required_custom

@login_required_custom
def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'home.html', context)
