from django.shortcuts import render
from django.http.response import HttpResponse


def home(request):
    """Returns the homepage of our reels website

    Args:
        request (HttpRequest): an instance of HttpRequest object.
    """
    return HttpResponse("<h1>COREELS HOMEPAGE</h1>")
