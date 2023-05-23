from django.shortcuts import render, get_object_or_404, redirect
from .models import Album
from .forms import AlbumForm


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'music/album_list.html', {'albums': albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'music/album_detail.html', {'album': album})


def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    return redirect('album_list')


def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            album = form.save(commit=False)
            album.save()
            return redirect('album-detail', pk=album.pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'edit-album'), {'form': form}


def create_album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(request.POST)
        form.save()
        return redirect('album_list')
    return render(request, 'music/new_album.html', {'form': form})
