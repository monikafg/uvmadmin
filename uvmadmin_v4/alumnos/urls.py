from django.urls import path
from .views import AlumnoListView, AlumnoDetailView, AlumnoUpdate, AlumnoCreate, AlumnoDelete

alumnos_patterns = ([
    path('', AlumnoListView.as_view(), name='alumnos'),  
    path('<int:pk>/', AlumnoDetailView.as_view(), name='alumno'),
    path('crear/', AlumnoCreate.as_view(), name='crear'),
    path('editar/<int:pk>/', AlumnoUpdate.as_view(), name='editar'),
    path('borrar/<int:pk>/', AlumnoDelete.as_view(), name='borrar'),
], 'alumnos')
