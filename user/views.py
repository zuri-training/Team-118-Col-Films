from django.conf import settings
from django.shortcuts import render, redirect

from user.forms import CreateUserForm


def register(request):
    """Register new user view.

    Registers new user into the user model upon verifying that user data
    are correct and valid."""

    #  If POST request method.
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():  # Is all field valid?
            new_user = form.save()
            return redirect(settings.LOGIN_URL)
        return render(request, 'registration/signup.html', {'form': form})

    else:
        form = CreateUserForm()  # Render empty user registration form.
    return render(request, "registration/signup.html", {"form": form})
