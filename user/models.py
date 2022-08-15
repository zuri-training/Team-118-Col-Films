from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


username_validator = UnicodeUsernameValidator()

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
    fullname = models.CharField(_("full name"), max_length=150, blank=True)
    username = models.CharField(
        _("username"), max_length=150, unique=True, null=True, blank=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    college_id = models.ImageField(
        _('College ID'), upload_to='verification', null=True, blank=True,
    )
    is_verified = models.BooleanField(
        _("college student status"), default=False,
        help_text=_("Designates whether user is verified college student."),
    )

    objects = UserModelManager()

    def __str__(self):
        return self.email

    def full_name(self):
        """Returns user's fullname or username"""
        if self.get_full_name():
            return self.get_full_name()
        return self.username.strip()

    class Meta:
        ordering = ['-date_joined', 'username']
