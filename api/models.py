from django.db import models

from django.db import models

class Item(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
class Categoria(models.Model):
    titulo = models.CharField(max_length=50)
    itens = models.ManyToManyField(Item, related_name='categorias')

    def __str__(self):
        return self.titulo