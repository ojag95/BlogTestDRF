# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from usuarios.models import Usuarios
from usuarios.serializers import UsuariosSerializer

@api_view(['GET', 'POST'])
def lista_usuarios(request, format=None):
    """
    Lista todos los usuarios
    """
    if request.method == 'GET':
        usuarios = Usuarios.objects.all()
        serializador = UsuariosSerializer(usuarios, many=True)
        return  Response(serializador.data)

    elif request.method == 'POST':
        serializador = UsuariosSerializer(data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)  
    
      
@api_view(['GET', 'PUT', 'DELETE'])
def detalle_usuarios(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    
    try:
        usuario = Usuarios.objects.get(pk=pk)
    except Usuarios.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializador = UsuariosSerializer(usuario)
        return Response(serializador.data)

    elif request.method == 'PUT':
        serializador = UsuariosSerializer(usuario, data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)