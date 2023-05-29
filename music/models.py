from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User


class Album(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    published_date = models.DateField(blank=True, null=True)
    band = models.ForeignKey(
        to='Band', on_delete=models.CASCADE, blank=True, null=True)
    cover = models.ImageField(upload_to='images/')
    user_favorite = models.ManyToManyField(User, default=None, blank=True)

    def __str__(self):
        return self.title


class Band(models.Model):
    name = models.CharField(max_length=200)
    solo = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'bands'

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=200)
    band = models.ForeignKey(
        to='Band', on_delete=models.CASCADE, blank=True, null=True)
    album = models.ForeignKey(
        to='Album', on_delete=models.CASCADE, blank=True, null=True, related_name='songs')
    preview = models.CharField(max_length=5000)

    def __str__(self):
        return self.name


class Favorite(models.Model):
    listener = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(to='Album', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
