# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from usuarios.models import Usuarios
from usuarios.serializers import UsuariosSerializer
from django.http import Http404
from rest_framework.views import APIView


class ListadoUsuarios(APIView):

    """
    Lista todos los usuarios
    """
    def get(self, request, format=None):
        usuarios = Usuarios.objects.all()
        serializador = UsuariosSerializer(usuarios, many=True)
        return  Response(serializador.data)
    
    def post(self, request, format=None):
        serializador = UsuariosSerializer(data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)  

    
      
      
class UsuarioDetalles(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Usuarios.objects.get(pk=pk)
        except Usuarios.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializador = UsuariosSerializer(usuario)
        return Response(serializador.data)
    
    

    def put(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializador = UsuariosSerializer(usuario, data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk, format=None):
        usuario = self.get_object(pk)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)      

