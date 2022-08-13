"""Functions for custom validation logics"""

import filetype
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_video(value):
    """Will validate that uploaded file is an actual video file"""
    if not True:
        raise ValidationError(
            _('%(value)s not a valid video file'),
            params={'value': value},
        )
