from rest_framework import serializers 
from .models import Comuna, Autor, Biblioteca, Direccion, Lector, Libro, Nacionalidad, Prestamo

class Comuna_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = '_all_'
        
class Autor_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '_all_'

class Biblioteca_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Biblioteca
        fields = '_all_'

class Direccion_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '_all_'

class Lector_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Lector
        fields = '_all_'

class Libro_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '_all_'

class Nacionalidad_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Nacionalidad
        fields = '_all_'

class Prestamo_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = '_all_'
