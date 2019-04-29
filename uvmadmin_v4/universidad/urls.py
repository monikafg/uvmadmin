from django.urls import path
from .views import (OrganizadorListView, OrganizadorDetailView, OrganizadorCreate, 
                    OrganizadorUpdate, OrganizadorDelete)

universidad_patterns = ([
    path('', OrganizadorListView.as_view(), name='organizadores'),
    path('<int:pk>/<slug:slug>/', OrganizadorDetailView.as_view(), name='organizador'),
    path('crear/', OrganizadorCreate.as_view(), name='crear'),
    path('editar/<int:pk>/', OrganizadorUpdate.as_view(), name='editar'),
    path('borrar/<int:pk>/', OrganizadorDelete.as_view(), name='borrar'),
], 'universidad')