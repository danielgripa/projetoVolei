from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from ..models import Professor
from ..serializers import UserSerializer, ProfessorSerializer

class AdicionarProfessor(APIView):
    def post(self, request, format=None):
        user_serializer = UserSerializer(data=request.data.get('user'))
        professor_serializer = ProfessorSerializer(data=request.data.get('professor'))

        if user_serializer.is_valid() and professor_serializer.is_valid():
            user = user_serializer.save()
            professor = professor_serializer.save(user=user)
            return Response({
                'user': UserSerializer(user).data,
                'professor': ProfessorSerializer(professor).data
            }, status=status.HTTP_201_CREATED)
        else:
            errors = user_serializer.errors
            errors.update(professor_serializer.errors)
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

class ListarProfessores(APIView):
    def get(self, request, format=None):
        professores = Professor.objects.select_related('user').all()
        serializer = ProfessorSerializer(professores, many=True)
        return Response(serializer.data)

class DetalhesProfessor(APIView):
    def get_object(self, user_id):
        try:
            return Professor.objects.select_related('user').get(user_id=user_id)
        except Professor.DoesNotExist:
            raise Http404

    def get(self, request, user_id, format=None):
        professor = self.get_object(user_id)
        serializer = ProfessorSerializer(professor)
        return Response(serializer.data)

class EditarProfessor(APIView):
    def get_object(self, user_id):
        try:
            return Professor.objects.get(user_id=user_id)
        except Professor.DoesNotExist:
            raise Http404

    def put(self, request, user_id, format=None):
        professor = self.get_object(user_id)
        user_serializer = UserSerializer(professor.user, data=request.data.get('user'))
        professor_serializer = ProfessorSerializer(professor, data=request.data.get('professor'))

        if user_serializer.is_valid() and professor_serializer.is_valid():
            user_serializer.save()
            professor_serializer.save()
            return Response({
                'user': user_serializer.data,
                'professor': professor_serializer.data
            })
        else:
            errors = user_serializer.errors
            errors.update(professor_serializer.errors)
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

class ExcluirProfessor(APIView):
    def get_object(self, user_id):
        try:
            return Professor.objects.get(user_id=user_id)
        except Professor.DoesNotExist:
            raise Http404

    def delete(self, request, user_id, format=None):
        professor = self.get_object(user_id)
        professor.user.delete()  # Isto também exclui o professor devido ao on_delete=models.CASCADE
        return Response(status=status.HTTP_204_NO_CONTENT)
