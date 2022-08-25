"""Module containing URL partterns for our reel app"""

from django.urls import path

from reel import views
from .views import IndexView, CreateVideo, VideoDetail, UpdateVideo, DeleteVideo, about

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('create/', CreateVideo.as_view(), name='upload'),
    path('<int:pk>/', VideoDetail.as_view(), name='video-detail'),
    path('<int:pk>/update/', UpdateVideo.as_view(), name='update-video'),
    path('<int:pk>/delete/', DeleteVideo.as_view(), name='delete-video'),
    path('explore/', views.explore, name='explore'),
    path('team/', views.team, name='team'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faqs/', views.faqs, name='faqs'),
]
