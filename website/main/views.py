from django.shortcuts import render, get_object_or_404
from .models import Post, Reply
from users.decorators import login_required_custom
from django.http import HttpResponse

@login_required_custom
def home(request):
    submit = False
    
    if request.GET.get('reply'):
        try:
            Reply.objects.create(
                post = Post.objects.get(pk=int(request.GET.get('reply'))),
                text = request.GET.get('text'),
                user_ip = request.META.get('REMOTE_ADDR'),
                creator = request.user
            )
            return HttpResponse('success')
        except: return HttpResponse('error')

    if request.method == "POST":
        Post.objects.create(
            title = request.POST['title'],
            body = request.POST['description'],
            topic = request.GET.get('topic','a'),
            creator = request.user,
            user_ip = request.META.get('REMOTE_ADDR')
        )
        submit = True

    context = {
        'posts':Post.objects.filter(topic=request.GET.get('topic','a')).order_by('-pk'),
        'topics': Post.TOPIC_CHOICES,
        'submit': submit
    }
    return render(request, 'home.html', context)

def install(request):
    return render(request,'install.html')

def set_location(request):
    try:
        user = request.user
        user.last_location = request.GET['c']
        user.save()
        return HttpResponse('success')
    except:
        return HttpResponse('error')