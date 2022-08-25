from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, reverse
from django.views.generic import TemplateView
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)
from django.utils.translation import gettext_lazy as _

from .models import Reel


class IndexView(ListView):
    model = Reel
    context_object_name = "reels"
    template_name = "reel/home.html"
    order_by = "-date_posted"


# Restricting the create video page to only logged in users
class CreateVideo(LoginRequiredMixin, CreateView):
    model = Reel
    fields = [
        'video'
    ]
    template_name = "reel/upload.html"

    def form_valid(self, form):
        if self.request.user.is_verified: # Is user a verified college student?
            form.instance.uploader = self.request.user
            return super().form_valid(form)
        
        # If user is not verified.
        form.add_error(None, ValidationError(
            _("Only verified college students can upload videos"),
            code='user_error'
        ))
        return render(self.request, self.template_name, {'form': form})

    def get_success_url(self):
        return reverse('update-video', kwargs={'pk': self.object.pk})


class VideoDetail(DetailView):
    model = Reel
    context_object_name = 'reel'
    template_name = "reel/player.html"

# Restricting the update video page to only logged in users
class UpdateVideo(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Reel
    fields = [
        'title', 'description', 'category', 'cover_thumbnail', 'published'
    ]
    template_name = "reel/update-reel.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reel'] = self.get_object()
        return context

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
    reels = Reel.objects.all()
    return render(request, 'reel/explore.html', {'reels': reels})


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
