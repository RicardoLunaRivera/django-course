from django.urls import path
from Aplicaciones.Academico.views import CursoListView, eliminar_curso, registrar_curso

urlpatterns = [
    path('', CursoListView.as_view(), name='gestion_cursos'),
    path('eliminarCurso/<int:id>', eliminar_curso),
    path("registrarCurso/", registrar_curso)
]
