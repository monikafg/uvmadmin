from django.urls import path
from .views import NoticiaListView, NoticiaDetailView, NoticiaCreate, NoticiaUpdate, NoticiaDelete

noticias_patterns = ([
    path('', NoticiaListView.as_view(), name='noticias'),
    path('<int:pk>/<slug:slug>/', NoticiaDetailView.as_view(), name='noticia'),
    path('crear/', NoticiaCreate.as_view(), name='crear'),
    path('editar/<int:pk>/', NoticiaUpdate.as_view(), name='editar'),
    path('borrar/<int:pk>/', NoticiaDelete.as_view(), name='borrar'),
], 'noticias')