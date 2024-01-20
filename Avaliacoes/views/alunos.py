from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Aluno
from ..serializers import AlunoSerializer
from django.http import Http404


class AdicionarAluno(APIView):
    def post(self, request, format=None):
        serializer = AlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListarAlunos(APIView):
    def get(self, request, format=None):
        alunos = Aluno.objects.all()
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)
    
    
class DetalhesAluno(APIView):
    def get_object(self, id):
        try:
            return Aluno.objects.get(pk=id)
        except Aluno.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        aluno = self.get_object(id)
        serializer = AlunoSerializer(aluno)
        return Response(serializer.data)



class EditarAluno(APIView):
    def get_object(self, id):
        try:
            return Aluno.objects.get(pk=id)
        except Aluno.DoesNotExist:
            raise Http404

    def put(self, request, id, format=None):
        aluno = self.get_object(id)
        serializer = AlunoSerializer(aluno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExcluirAluno(APIView):
    def get_object(self, id):
        try:
            return Aluno.objects.get(pk=id)
        except Aluno.DoesNotExist:
            raise Http404

    def delete(self, request, id, format=None):
        aluno = self.get_object(id)
        aluno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
