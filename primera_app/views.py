from django.shortcuts import render
from rest_framework import viewsets
from .serializer import Comuna_Serializer, Autor_Serializer, Biblioteca_Serializer, Direccion_Serializer, Lector_Serializer, Libro_Serializer, Nacionalidad_Serializer, Prestamo_Serializer
from .models import Comuna, Autor, Biblioteca, Direccion, Lector, Libro, Nacionalidad, Prestamo

# Create your views here.
class Comuna_ViewSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = Comuna_Serializer

class Autor_ViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = Autor_Serializer

class Biblioteca_ViewSet(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    serializer_class = Biblioteca_Serializer

class Direccion_ViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = Direccion_Serializer

class Lector_ViewSet(viewsets.ModelViewSet):
    queryset = Lector.objects.all()
    serializer_class = Lector_Serializer

class Libro_ViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = Libro_Serializer

class Nacionalidad_ViewSet(viewsets.ModelViewSet):
    queryset = Nacionalidad.objects.all()
    serializer_class = Nacionalidad_Serializer

class Prestamo_ViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = Prestamo_Serializer