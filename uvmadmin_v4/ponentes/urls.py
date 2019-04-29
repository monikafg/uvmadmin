from django.urls import path
from .views import PonenteListView, PonenteDetailView, PonenteUpdate, PonenteCreate, PonenteDelete

ponentes_patterns = ([
    path('', PonenteListView.as_view(), name='ponentes'),  
    path('<int:pk>/', PonenteDetailView.as_view(), name='ponente'),
    path('crear/', PonenteCreate.as_view(), name='crear'),
    path('editar/<int:pk>/', PonenteUpdate.as_view(), name='editar'),
    path('borrar/<int:pk>/', PonenteDelete.as_view(), name='borrar'),
], 'ponentes')