from django.urls import path

from gallery.views import (AlbumView, AlbumList, 
                           AlbumCreate, AlbumDelete, AlbumUpdate)

app_name = 'gallery'
urlpatterns = [
    path('', AlbumList.as_view(), name='album_list'),
    path('album/<int:pk>/<slug>/', AlbumView.as_view(), name='album_detail'),
    path('borrar/<int:pk>/', AlbumDelete.as_view(), name='album_delete'),
    path('crear/', AlbumCreate.as_view(), name='album_create'),
    path('editar/<int:pk>/', AlbumUpdate.as_view(), name='album_update'),
]
