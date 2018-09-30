from rest_framework import serializers
from usuarios.models import Usuarios
"""DEPRECATED 
class UsuariosSerializer(serializers.Serializer):
    #The first part of the serializer class defines the fields 
    #that get serialized/deserialized.
    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(required=False, max_length=50)
    apellidoP=serializers.CharField(required=False, max_length=50)
    apellidoM=serializers.CharField(required=False, max_length=50)
    correo=serializers.EmailField(required=False)
    usuario=serializers.CharField(required=False)
    contrasenia=serializers.CharField(required=False)
    created= serializers.DateTimeField(required=False)
    #The create() and update() methods define how fully fledged 
    #instances are created or modified when calling serializer.save()
    
    def create(self, validated_data):
    
    #    Create and return a new `Snippet` instance, given the validated data.
        
        return Usuarios.objects.create(**validated_data)

    def update(self, instance, validated_data):
       
       # Update and return an existing `Snippet` instance, given the validated data.
        
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.apellidoP = validated_data.get('apellidoP', instance.apellidoP)
        instance.apellidoM = validated_data.get('apellidoM', instance.apellidoM)
        instance.correo = validated_data.get('correo', instance.correo)
        instance.usuario = validated_data.get('usuario', instance.usuario)
        instance.contrasenia = validated_data.get('contrasenia', instance.contrasenia)
        instance.created=validated_data.get('created',instance.created)
        instance.save()
        return instance
DEPRECATED"""
class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ('id', 'nombre', 'apellidoP', 'apellidoM', 'correo', 'usuario','contrasenia')
