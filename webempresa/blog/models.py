from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length = 100)
    created = models.DateTimeField(auto_now_add = True, verbose_name = 'Fecha de Creacion')
    updated = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de Edicion')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    

    def __str__(self):
        return self.name


class Post(models.Model):

    tittle = models.CharField(max_length=200, verbose_name = 'Titulo')
    content = models.TextField(verbose_name ='Contenido')
    published = models.DateTimeField(verbose_name ='Fecha de Publicacion', default = now)
    image = models.ImageField(verbose_name = 'Imagen', upload_to = 'blog', null = True, blank = True)
    author = models.ForeignKey(User, verbose_name='Autor', on_delete= models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name = 'Categoria', related_name= "get_posts")
    created = models.DateTimeField(auto_now_add = True, verbose_name = 'Fecha de Creacion')
    updated = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de Edicion')

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
    

    def __str__(self):
        return self.tittle