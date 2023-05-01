from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    legajo = models.IntegerField()
    fecha_nacimiento = models.DateField()
    
    def __str__(self):
        return f'Nombre:{self.nombre} - Apellido:{self.apellido}'
    
class CategoriaProducto(models.Model):
    nombre_categoria = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_categoria

class Producto(models.Model):
    # nombre_categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    item = models.CharField(max_length=20)
    descripcion= RichTextField()
    cantidad = models.IntegerField()
    foto = models.ImageField(blank=True)
    
    def __str__(self):
        return f'{self.item}'
    