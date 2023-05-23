from django.db import models
from django.conf import settings
from django.utils import timezone


class Album(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    songs = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    published_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
