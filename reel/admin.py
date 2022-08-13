from django.contrib import admin

from reel import models


admin.site.register([
    models.Reel, models.Comment, models.Like, models.Dislike, models.View,
    models.Category
])
