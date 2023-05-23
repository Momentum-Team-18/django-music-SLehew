from django.shortcuts import render, get_object_or_404, redirect
from .models import Album
from .forms import AlbumForm


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'music/album_list.html', {'albums': albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'music/album_detail.html', {'album': album})


def create_album(request):
    form = AlbumForm()
    return render(request, 'music/new_album.html', {'form': form})
