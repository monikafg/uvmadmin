from django.urls import path
from .views import (MatriculaListView, MatriculaDetailView, MatriculaCreate, 
                    MatriculaUpdate, MatriculaDelete)

matriculas_patterns = ([
    path('', MatriculaListView.as_view(), name='matriculas'),  
    path('<int:pk>/', MatriculaDetailView.as_view(), name='matricula'),
    path('crear/', MatriculaCreate.as_view(), name='crear'),
    path('editar/<int:pk>/', MatriculaUpdate.as_view(), name='editar'),
    path('borrar/<int:pk>/', MatriculaDelete.as_view(), name='borrar'),
], 'matriculas')