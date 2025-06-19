from django.shortcuts import redirect
from django.urls import reverse

class InstallMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.GET.get('pwa') or request.session.get('pwa'):
            if request.GET.get('pwa'):
                request.session['pwa'] = request.GET.get('pwa')

            if not request.user.is_authenticated and not 'login' in request.path and not 'register' in request.path:
                return redirect(reverse('login'))

        if not request.GET.get('pwa') and not request.session.get('pwa') and not 'install' in request.path:
            return redirect(reverse('install'))

        return self.get_response(request)

