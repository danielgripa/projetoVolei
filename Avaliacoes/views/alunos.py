from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from ..models import Aluno
from ..serializers import AlunoSerializer, UserSerializer


class AdicionarAluno(APIView):
    def post(self, request, format=None):
        user_serializer = UserSerializer(data=request.data.get('user'))
        aluno_serializer = AlunoSerializer(data=request.data.get('aluno'))

        if user_serializer.is_valid() and aluno_serializer.is_valid():
            user = user_serializer.save()
            aluno = aluno_serializer.save(user=user)
            return Response({
                'user': UserSerializer(user).data,
                'aluno': AlunoSerializer(aluno).data
            }, status=status.HTTP_201_CREATED)
        else:
            errors = user_serializer.errors
            errors.update(aluno_serializer.errors)
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)




class ListarAlunos(APIView):
    def get(self, request, format=None):
        alunos = Aluno.objects.select_related('user').all()
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)

class DetalhesAluno(APIView):
    def get_object(self, id):
        try:
            return Aluno.objects.select_related('user').get(pk=id)
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
        user_serializer = UserSerializer(aluno.user, data=request.data.get('user'))
        aluno_serializer = AlunoSerializer(aluno, data=request.data.get('aluno'))

        if user_serializer.is_valid() and aluno_serializer.is_valid():
            user_serializer.save()
            aluno_serializer.save()
            return Response({
                'user': user_serializer.data,
                'aluno': aluno_serializer.data
            })
        else:
            errors = user_serializer.errors
            errors.update(aluno_serializer.errors)
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)


class ExcluirAluno(APIView):
    def get_object(self, id):
        try:
            return Aluno.objects.get(pk=id)
        except Aluno.DoesNotExist:
            raise Http404

    def delete(self, request, id, format=None):
        aluno = self.get_object(id)
        aluno.user.delete()  # Isto também exclui o aluno devido ao on_delete=models.CASCADE
        return Response(status=status.HTTP_204_NO_CONTENT)

