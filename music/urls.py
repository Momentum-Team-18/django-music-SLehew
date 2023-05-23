from django.urls import path
from . import views


urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('album/<int:pk>', views.album_detail, name='album-detail'),
    path('album/new', views.create_album, name="album-new")
]
