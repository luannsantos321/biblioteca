from pyexpat import model
from django.db import models

# Create your models here.



class Autor(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=80)

    def __str__(self) -> str:
        return self.nome

    class Meta:
        app_label = "livros"
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ['nome']

class Livro(models.Model):
    autor = models.ForeignKey(Autor,verbose_name="Autor", on_delete=models.CASCADE)
    nome = models.CharField(verbose_name = "Nome", max_length=80)

    def __str__(self) -> str:
        return self.nome

    class Meta:
        app_label = "livros"
        verbose_name = "Livro"
        verbose_name_plural = "Livros"
        ordering = ['nome']