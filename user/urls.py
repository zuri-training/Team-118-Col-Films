"""Define URL patterns for the users and related profiles."""


from django.urls import path
from user import views


urlpatterns = [
    path('register/', views.register, name="register"),
]
