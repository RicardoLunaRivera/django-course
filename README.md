# Curso Django

Es un framework de Python para crear aplicaciones web, comenxxo a desarrollarse en el año de 2002,
pero se publica de forma oficial en el 2005.

Fomenta el desarrollo rápido y diseño limpio y pragmático ( muy ligado a la resolución de problemas en la práctica).
Muy apegado a la filosofia DRY ( Don't Repeat Yourself).

Sigue el modelo de arquitectura MTV( Model Template View).

- Modelo : Manipula los datos en la aplicación
- Template : Decide como se verán los datos en el navegador.
- View : Decide cuáles datos va a mostrar el template.

```sh
 pip intall django # instalar django

 django-admin startproject <name_project> # crear un proyecto

 python manage.py runserver # par ainiciar el servidor de django
```

![alt](./imgs/Estructura_project_django.png)

- init.py -> Indica a python que la carpeta es un paquete
- asgi.py -> Asynchronous Server Gateway Interface
- wsgi.py Web Server Gateway Interface
- settings.py -> configuraciones del proyecto
- urls.py -> URLS del proyecto
- views.py -> vistas para el proyecto
