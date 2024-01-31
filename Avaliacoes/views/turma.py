from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Turma
from ..serializers import TurmaSerializer
from django.http import Http404
from django.shortcuts import get_object_or_404


class AdicionarTurma(APIView):
    def post(self, request, format=None):
        serializer = TurmaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListarTurmas(APIView):
    def get(self, request, format=None):
        turmas = Turma.objects.all()
        serializer = TurmaSerializer(turmas, many=True)
        return Response(serializer.data)

class DetalhesTurma(APIView):
    def get_object(self, id):
        try:
            return Turma.objects.get(pk=id)
        except Turma.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        turma = self.get_object(id)
        serializer = TurmaSerializer(turma)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        turma = self.get_object(id)
        serializer = TurmaSerializer(turma, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        turma = self.get_object(id)
        turma.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EditarTurma(APIView):
    def put(self, request, id, format=None):
        turma = get_object_or_404(Turma, pk=id)
        serializer = TurmaSerializer(turma, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExcluirTurma(APIView):
    def delete(self, request, id, format=None):
        turma = get_object_or_404(Turma, pk=id)
        turma.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
