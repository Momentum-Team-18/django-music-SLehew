from django.urls import path
from . import views
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('album/<int:pk>', views.album_detail, name='album-detail'),
    path('album/new', views.create_album, name="album-new"),
    path('album/<int:pk>/delete', views.delete_album, name='delete-album'),
    path('album/<int:pk>/edit', views.edit_album, name='edit-album'),
    path('fav/<int:id>/', views.favorite_add, name='favorite-add'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
