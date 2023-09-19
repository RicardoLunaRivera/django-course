from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Curso
from django.views.generic import ListView

# Create your views here.

# Vista basada en Funciones


def home(request):
    cursos_listado = Curso.objects.all().order_by('nombre')
    # cursos_listado = Curso.objects.all().order_by('nombre', 'creditos') #El segundo criterio de ordenamiento son los créditos
    # cursos_listado = Curso.objects.all().order_by('-nombre') # Decreciente
    # cursos_listado = Curso.objects.all()[:5] # Muestra los primeros 5
    # cursos_listado = Curso.objects.filter(nombre='Español') # Filtra por un nombre en especial
    # cursos_listado = Curso.objects.filter(creditos__gte=5) # filtro mayor o igual que
    # cursos_listado = Curso.objects.filter(creditos__lte=4)  # filtro menor o igual que
    # Filtro para mostarr cursoq ue empiezan con una letra en especifico
    # cursos_listado = Curso.objects.filter(nombre__startswith='E')# return HttpResponse("<h1>Hola Mundo </h1>")

    data = {
        'titulo': 'Gestión de Cursos',
        'cursos': cursos_listado
    }

    # return render(request, "gestionCursos.html", {"cursos": cursos_listado})
    return render(request, "gestionCursos.html", data)


# Vista basada en modelos / en clases

class CursoListView(ListView):
    model = Curso
    template_name = 'gestionCursos.html'

    # filtro
    def get_queryset(self):
        return Curso.objects.filter(creditos__gte=0)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Gestion de Cursos'
        return context


def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()

    return redirect('/')


def registrar_curso(request):
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.create(nombre=nombre, creditos=creditos)

    return redirect('/')
