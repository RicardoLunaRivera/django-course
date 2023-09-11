from django.shortcuts import render
# from django.http import HttpResponse
from .models import Curso
# Create your views here.


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
    return render(request, "gestionCursos.html", {"cursos": cursos_listado})
