"""
URL configuration for django_test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django_test.views import bienvenida, bienvenida_blue, categoria_edad 
from django_test.views import fecha_actual
from django_test.views import contenido_html
from django_test.views import primer_plantilla
from django_test.views import plantilla_parametros
from django_test.views import plantilla_loader
from django_test.views import plantilla_shortcut# Se importa la vista
from django_test.views import plantilla_hija_uno
from django_test.views import plantilla_hija_dos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenida/', bienvenida),
    path('bienvenida_blue/', bienvenida_blue),
    path('categoria_edad/<int:edad>', categoria_edad),
    path('fecha/', fecha_actual),
    path('contenido_html/<nombre>/<int:edad>', contenido_html),
    path('primer_plantilla/', primer_plantilla),
    path('plantilla_parametros/', plantilla_parametros),
    path('plantilla_loader/', plantilla_loader),
    path('plantilla_shortcut/',plantilla_shortcut),# -> se crea la url de acceso a la vista
    path('plantilla_hija_uno/',plantilla_hija_uno),
    path('plantilla_hija_dos/',plantilla_hija_dos),
]
