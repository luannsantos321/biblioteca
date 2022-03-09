from django.contrib import admin
from livros.models import Livro, Autor
# Register your models here.
@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    pass

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    pass