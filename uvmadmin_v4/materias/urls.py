from django.urls import path
from .views import (MateriaListView, MateriaDetailView, MateriaCreate, 
                    MateriaUpdate, MateriaDelete, MateriaPonentesUpdate, 
                    MateriaApuntesCreate, MateriaApuntesDelete, MateriaApuntesUpdate,
                    MateriaPonenciaCreate, MateriaPonenciaDelete, MateriaPonenciaUpdate)

materias_patterns = ([
    path('', MateriaListView.as_view(), name='materias'),
    path('<int:pk>/', MateriaDetailView.as_view(), name='materia'),
    path('crear/', MateriaCreate.as_view(), name='crear'),
    path('editar/<int:pk>/', MateriaUpdate.as_view(), name='editar'),
    path('borrar/<int:pk>/', MateriaDelete.as_view(), name='borrar'),
    path('ponentes/<int:pk>/', MateriaPonentesUpdate.as_view(), name='ponente_add'),
    path('apuntes_add/<int:pk>/', MateriaApuntesCreate.as_view(), name='apuntes_add'),
    path('apuntes_del/<int:pk>/<int:mat>/', MateriaApuntesDelete.as_view(), name='apuntes_del'),
    path('apuntes_upd/<int:pk>/<int:mat>/', MateriaApuntesUpdate.as_view(), name='apuntes_upd'),
    path('ponencia_add/<int:pk>/', MateriaPonenciaCreate.as_view(), name='ponencia_add'),
    path('ponencia_del/<int:pk>/<int:mat>/', MateriaPonenciaDelete.as_view(), name='ponencia_del'),
    path('ponencia_upd/<int:pk>/<int:mat>/', MateriaPonenciaUpdate.as_view(), name='ponencia_upd'),
], 'materias')
