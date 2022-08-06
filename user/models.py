from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserModelManager(UserManager):
    """Force Case Insensitive Username Field.
    
    Extends UserManager to ensure that CaSe InsenSItiVE usernames are
    recognized as one."""

    def get_by_natural_key(self, username):
        """Enable caSe InsEnSiTive username look up."""
        anycase_username_field = f'{self.model.USERNAME_FIELD}__iexact'
        return self.get(**{anycase_username_field: username})


class UserModel(AbstractUser):
    """Implement custom user model.

    Define extra fields and assign UserModelManager as the default object
    manager.
    """
    is_verified = models.BooleanField(
        _("college student status"), default=False,
        help_text=_("Designates whether user is verified college student."),
    )

    objects = UserModelManager()

    def full_name(self):
        """Returns user's fullname or username"""
        if self.get_full_name():
            return self.get_full_name()
        return self.username.strip()

    class Meta:
        ordering = ['-date_joined', 'username']
