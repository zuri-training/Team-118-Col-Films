"""Module containing URL partterns for our reel app"""

from django.urls import path

# from reel import views
from reel import views as video_views
from .views import IndexView, CreateVideo, VideoDetail, UpdateVideo, DeleteVideo

urlpatterns = [
    # path('', views.home, name='home'),
    path('', IndexView.as_view(), name='index'),
    path('create/', CreateVideo.as_view(), name='create-video'),
    path('<int:pk>/', VideoDetail.as_view(), name='video-detail'),
    path('<int:pk>/update', UpdateVideo.as_view(), name='update-video'),
    path('<int:pk>/delete', DeleteVideo.as_view(), name='delete-video'),
]