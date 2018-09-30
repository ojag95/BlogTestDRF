# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from usuarios.models import Usuarios
from usuarios.serializers import UsuariosSerializer

@csrf_exempt
def lista_usuarios(request):
    """
    Lista todos los usuarios
    """
    if request.method == 'GET':
        usuarios = Usuarios.objects.all()
        serializador = UsuariosSerializer(usuarios, many=True)
        return JsonResponse(serializador.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializador = UsuariosSerializer(data=data)
        if serializador.is_valid():
            serializador.save()
            return JsonResponse(serializador.data, status=201)
        return JsonResponse(serializador.errors, status=400)
    
@csrf_exempt
def detalle_usuarios(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        usuario = Usuarios.objects.get(pk=pk)
    except Usuarios.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializador = UsuariosSerializer(usuario)
        return JsonResponse(serializador.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializador = UsuariosSerializer(usuario, data=data)
        if serializador.is_valid():
            serializador.save()
            return JsonResponse(serializador.data)
        return JsonResponse(serializador.errors, status=400)

    elif request.method == 'DELETE':
        usuario.delete()
        return HttpResponse(status=204)