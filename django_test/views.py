from django.http import HttpResponse
import datetime
from django.template import Template, Context
#from django.template import loader
from django.template.loader import get_template
from django.shortcuts import render
# Request: Para realizar peticiones
# httpResponse: ära enviar respuestas usando el protocolo HTTP

#Vista
def bienvenida(request): # Se manda un reques como argumento
    return HttpResponse("Hola Mundo desde Django")

def bienvenida_blue(request): # Se manda un reques como argumento
    return HttpResponse("<p style = 'color : blue;'> Hola Mundo desde Django Blue </p>")

def categoria_edad (request, edad):
    if edad >= 18:
        if edad >= 60:
            categoria = "Tercera edad"
        else:
            categoria = "Adultes"
    else:
        if edad < 10:
            categoria = "Niñes"
        else:
            categoria = "Adolescencia"
            
    resultado  = "<h1> Categoría de la edad: %s </h1>" %categoria
    return HttpResponse(resultado)

def fecha_actual(request):
    fecha = "<h1> Fecha y hora: {0}</h1>".format(datetime.datetime.now().strftime ("%A %d/%m/%Y %H:%M:%S"))
    return HttpResponse(fecha)

def contenido_html(request, nombre : str, edad : int):
    contenido = """
    <html>
    <body> 
    <h1> Nombre : %s  /  Edad: %s   </h1>
    </body>
    </html>
    """ % (nombre, edad)
    
    return HttpResponse(contenido)

def primer_plantilla(request):
    #Se abrer la plantilla HTML
    plantilla_externa = open("D:\Python Courses\django\django_test\plantillas\index.html")
    #Cargamos el documento a una variable de tipo Template
    template = Template(plantilla_externa.read())
    #Cerramos el documento externo
    plantilla_externa.close()
    #Se crea un contexto
    contexto = Context()
    #Se renderiza el documento
    documento = template.render(contexto)
    return HttpResponse(documento)


def plantilla_parametros(request):
    nombre = "Caliman"
    fecha_actual = datetime.datetime.now()
    lenguajes = ["Java", "Python", "C#", "JavaScript", "Kotlin", "Dart"]
    #Se abrer la plantilla HTML
    plantilla_externa = open("D:\Python Courses\django\django_test\plantillas\plantilla_parametrs.html")
    #Cargamos el documento a una variable de tipo Template
    template = Template(plantilla_externa.read())
    #Cerramos el documento externo
    plantilla_externa.close()
    #Se crea un contexto
    contexto = Context({"nombre" : nombre, "fecha_actual" : fecha_actual, "lenguajes": lenguajes})
    #Se renderiza el documento
    documento = template.render(contexto)
    return HttpResponse(documento)

def plantilla_loader(request):
    nombre = "Caliman"
    fecha_actual = datetime.datetime.now()
    lenguajes = ["Java", "Python", "C#", "JavaScript", "Kotlin", "Dart", "Rust"]
    #se especedica el nombre de la plantilla
    plantilla_externa = get_template('plantilla_parametrs.html')
    #renderizar el documento
    documento = plantilla_externa.render({"nombre" : nombre, "fecha_actual" : fecha_actual, "lenguajes": lenguajes})
    return HttpResponse(documento)

def plantilla_shortcut(request):
    nombre = "Caliman"
    fecha_actual = datetime.datetime.now()
    lenguajes = ["Java", "Python", "C#", "JavaScript", "Kotlin", "Dart", "Rust", "PHP"]
    
    return render(request, 'plantilla_parametrs.html',{"nombre" : nombre, "fecha_actual" : fecha_actual, "lenguajes": lenguajes})


def plantilla_hija_uno(request):
    return render(request, 'plantilla_hija_uno.html' )


def plantilla_hija_dos(request):
    return render(request, 'plantilla_hija_dos.html' )