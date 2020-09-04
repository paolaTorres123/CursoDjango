from django.db import models

# Create your models here.

class Project(models.Model):

    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to = "projects")
    link = models.URLField(null=True, blank=True, verbose_name="Direccion Web")
    created = models.DateTimeField(auto_now_add =True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")


    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"] #reverso de la ordenacion


    def __str__(self):
        return self.title

