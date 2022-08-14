from venv import create
from wsgiref.handlers import format_date_time
from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Reel
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    """Returns the homepage of our reels website

    Args:
        request (HttpRequest): an instance of HttpRequest object.
    """
    return HttpResponse("<h1>COREELS HOMEPAGE</h1>")


class IndexView(ListView):
    model = Reel
    template_name = "reel/home.html"
    order_by = "-date_posted"


class AboutView(TemplateView):
    template_name = "about.html"

# Restricting the create video page to only logged in users
class CreateVideo(LoginRequiredMixin, CreateView):
    model = Reel
    fields = ['title', 'description', 'video', 'cover_thumbnail']
    template_name = "create_video.html"

    def form_valid(self, form):
        form.instance.uploader = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('video-detail', kwargs={'pk': self.object.pk})


class VideoDetail(DetailView):
    model = Reel
    template_name = "video_detail.html"

# Restricting the update video page to only logged in users
class UpdateVideo(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Reel
    fields = ['title', 'description']
    template_name = "create_video.html"

    def get_success_url(self):
        return reverse('video-detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        video = self.get_object()
        return self.request.user == video.uploader

# Restricting the delete video page to only logged in users
class DeleteVideo(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Reel
    template_name = "delete_video.html"

    def get_success_url(self):
        return reverse("index")

    def test_func(self):
        video = self.get_object()
        return self.request.user == video.uploader

def explore(request):
    """Returns explore page"""
    return render(request, 'reel/explore.html', {})


def team(request):
    """Returns team page"""
    return render(request, 'reel/team.html', {})


def about(request):
    """Returns about page"""
    return render(request, 'reel/about.html', {})


def contact(request):
    """Returns contact page"""
    return render(request, 'reel/contact.html', {})


def faqs(request):
    """Returns FAQS page"""
    return render(request, 'reel/faqs.html', {})
