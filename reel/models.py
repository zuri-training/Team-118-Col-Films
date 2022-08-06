from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    """Represents each movie category"""

    name = models.CharField(
        _("category title"), max_length=155,
        help_text=_("enter short caegory name")
    )
    description = models.TextField(
        _("long description"), help_text=_("long category description")
    )
    date = models.DateTimeField(
        _("date added"), default=timezone.now,
        help_text="date category was created"
    )

    class Meta:
        ordering = ['-date', 'name']
        verbose_name_plural = 'categories'


    def __str__(self) -> str:
        return self.name


class Reel(models.Model):
    """Represents each reel/short video in collection"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_("uploaded by"),
        on_delete=models.CASCADE
    )
    name = models.CharField(
        _("video title"), max_length=255, help_text=_("enter video short name")
    )
    description = models.TextField(
        _("long description"), help_text=_("long video description")
    )
    category = models.ManyToManyField(
        Category, verbose_name=_("video category"),
        help_text=_("choose video category")
    )
    cover = models.ImageField(
        _("video cover"), upload_to="reels/cover", help_text=_("cover image"),
        null=True, blank=True
    )
    video = models.FileField(
        _("video file"), upload_to='reels', max_length=100,
        help_text=_("upload short video file less than 15 minutes"),
        validators=[FileExtensionValidator(allowed_extensions=[
            'MOV','avi','mp4','webm','mkv'
        ])]
    )
    date = models.DateTimeField(
        _("date uploaded"), default=timezone.now,
        help_text="date video was uploaded"
    )

    class Meta:
        ordering = ['-date', 'name']


    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    """Represents comment made on a reel"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_("commented by"),
        on_delete=models.CASCADE, related_name="commenter"
    )
    comment = models.TextField(
        help_text=_("comment on reels")
    )
    real = models.ForeignKey(
        Reel, verbose_name=_("comment on"), on_delete=models.CASCADE,
        help_text=_("reel commented on"), related_name="commented"
    )
    date = models.DateTimeField(
        _("date commented"), default=timezone.now,
        help_text="date comment was made"
    )

    class Meta:
        ordering = ['-date', 'user']


    def __str__(self) -> str:
        return f"{self.user} commented on: {self.real}"


class Favorite(models.Model):
    """Represents favorite made on a reel"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_("favorited by"),
        on_delete=models.CASCADE, related_name="favoriter"
    )
    real = models.ForeignKey(
        Reel, verbose_name=_("favorite on"), on_delete=models.CASCADE,
        help_text=_("reel being favorited"), related_name="favoriited"
    )
    date = models.DateTimeField(
        _("date favorited"), default=timezone.now,
        help_text="date favorite was added"
    )

    class Meta:
        ordering = ['-date', 'user']


    def __str__(self) -> str:
        return f"{self.user} favorited: {self.real}"


class Like(models.Model):
    """Represents like made on a reel"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_("liked by"),
        on_delete=models.CASCADE, related_name="liker"
    )
    real = models.ForeignKey(
        Reel, verbose_name=_("liked reel"), on_delete=models.CASCADE,
        help_text=_("reel liked"), related_name="liked"
    )
    date = models.DateTimeField(
        _("date liked"), default=timezone.now,
        help_text="date like was recorded"
    )

    class Meta:
        ordering = ['-date', 'user']


    def __str__(self) -> str:
        return f"{self.user} liked: {self.real}"


class Dislike(models.Model):
    """Represents dislike made on a reel"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_("disliked by"),
        on_delete=models.CASCADE, related_name="disliker"
    )
    real = models.ForeignKey(
        Reel, verbose_name=_("disliked reel"), on_delete=models.CASCADE,
        help_text=_("reel disliked"), related_name="disliked"
    )
    date = models.DateTimeField(
        _("date disliked"), default=timezone.now,
        help_text="date dislike was recorded"
    )

    class Meta:
        ordering = ['-date', 'user']


    def __str__(self) -> str:
        return f"{self.user} disliked: {self.real}"


class View(models.Model):
    """Represents view made on a reel"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_("viewed by"),
        on_delete=models.CASCADE, related_name="viewer"
    )
    real = models.ForeignKey(
        Reel, verbose_name=_("viewed reel"), on_delete=models.CASCADE,
        help_text=_("reel viewed")
    )
    date = models.DateTimeField(
        _("date viewed"), default=timezone.now,
        help_text="date view was made"
    )

    class Meta:
        ordering = ['-date', 'user']


    def __str__(self) -> str:
        return f"{self.user} viewed: {self.real}"
