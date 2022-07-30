"""Module containing URL partterns for our reel app"""

from django.urls import path

from reel import views

urlpatterns = [
    path('', views.home, name='home')
]