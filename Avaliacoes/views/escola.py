from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Escola
from ..serializers import EscolaSerializer
from django.http import Http404
from django.shortcuts import get_object_or_404


class AdicionarEscola(APIView):
    def post(self, request, format=None):
        serializer = EscolaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListarEscolas(APIView):
    def get(self, request, format=None):
        escolas = Escola.objects.all()
        serializer = EscolaSerializer(escolas, many=True)
        return Response(serializer.data)

class DetalhesEscola(APIView):
    def get_object(self, id):
        try:
            return Escola.objects.get(pk=id)
        except Escola.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        escola = self.get_object(id)
        serializer = EscolaSerializer(escola)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        escola = self.get_object(id)
        serializer = EscolaSerializer(escola, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        escola = self.get_object(id)
        escola.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EditarEscola(APIView):
    def put(self, request, id, format=None):
        escola = get_object_or_404(Escola, pk=id)
        serializer = EscolaSerializer(escola, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExcluirEscola(APIView):
    def delete(self, request, id, format=None):
        escola = get_object_or_404(Escola, pk=id)
        escola.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)