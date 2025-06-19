from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('install/', views.install, name='install'),
    path('set-location/', views.set_location, name='set-location'),
]
