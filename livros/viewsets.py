from rest_framework import viewsets
from livros.serializers import LivroSerializer, AutorSerializer
from livros.models import Livro,Autor

class LivroViewset(viewsets.ModelViewSet):
    serializer_class = LivroSerializer
    queryset = Livro.objects.all()

class AutorViewset(viewsets.ModelViewSet):
    serializer_class = AutorSerializer
    queryset = Autor.objects.all()