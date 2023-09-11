from django.db import models

# Create your models here.


class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0} ({1})".format(self.nombre, self.creditos)
        return texto
