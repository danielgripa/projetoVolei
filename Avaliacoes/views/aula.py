from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Aula
from ..serializers import AulaSerializer
from django.http import Http404
from django.shortcuts import get_object_or_404


class AdicionarAula(APIView):
    def post(self, request, format=None):
        serializer = AulaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListarAulas(APIView):
    def get(self, request, format=None):
        aulas = Aula.objects.all()
        serializer = AulaSerializer(aulas, many=True)
        return Response(serializer.data)

class DetalhesAula(APIView):
    def get_object(self, id):
        try:
            return Aula.objects.get(pk=id)
        except Aula.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        aula = self.get_object(id)
        serializer = AulaSerializer(aula)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        aula = self.get_object(id)
        serializer = AulaSerializer(aula, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        aula = self.get_object(id)
        aula.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class EditarAula(APIView):
    def put(self, request, id, format=None):
        aula = get_object_or_404(Aula, pk=id)
        serializer = AulaSerializer(aula, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExcluirAula(APIView):
    def delete(self, request, id, format=None):
        aula = get_object_or_404(Aula, pk=id)
        aula.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)