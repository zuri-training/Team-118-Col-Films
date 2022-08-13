# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from user.models import UserModel


class CreateUserForm(UserCreationForm):
    """Enable Case Insensitive Validation of username
    
    Extends UserCreationForm to enable caSe-InseSiTiVe validation of
    username"""

    def clean(self):
        """Perform custom form validation."""

        cleaned_data = super(CreateUserForm, self).clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')

        if UserModel.objects.filter(username__iexact=username).exists():
            self.add_error('username', ValidationError(
                _('A user with %(username)s already exists.'),
                code='username_error', params={'username': username}
            ))
        if UserModel.objects.filter(email__iexact=email).exists():
            self.add_error('email', ValidationError(
                _('Email address %(email)s already in use.'),
                code='email_error', params={'email', email}
            ))

        return cleaned_data

    class Meta:
        model = UserModel
        fields = [
            "first_name", "last_name", "username", "email",
        ]


class ChangeUserForm(UserChangeForm):
    """Ensure that the correct model is used for changing user details"""

    class Meta:
        model = UserModel
        fields = ["username", "email"]
