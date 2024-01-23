from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Avaliacao, Aluno, AtributoFundamento
from ..serializers import AvaliacaoSerializer
from django.http import Http404

class ListarAvaliacoes(APIView):
    def get(self, request, format=None):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

class DetalhesAvaliacao(APIView):
    def get_object(self, idaluno, idatributo):
        try:
            return Avaliacao.objects.get(idaluno=idaluno, idatributo=idatributo)
        except Avaliacao.DoesNotExist:
            raise Http404

    def get(self, request, idaluno, idatributo, format=None):
        avaliacao = self.get_object(idaluno, idatributo)
        serializer = AvaliacaoSerializer(avaliacao)
        return Response(serializer.data)

class AdicionarAvaliacao(APIView):
    def post(self, request, format=None):
        serializer = AvaliacaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditarAvaliacao(APIView):
    def get_object(self, idaluno, idatributo):
        try:
            return Avaliacao.objects.get(idaluno=idaluno, idatributo=idatributo)
        except Avaliacao.DoesNotExist:
            raise Http404

    def put(self, request, idaluno, idatributo, format=None):
        avaliacao = self.get_object(idaluno, idatributo)
        serializer = AvaliacaoSerializer(avaliacao, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExcluirAvaliacao(APIView):
    def get_object(self, idaluno, idatributo):
        try:
            return Avaliacao.objects.get(idaluno=idaluno, idatributo=idatributo)
        except Avaliacao.DoesNotExist:
            raise Http404

    def delete(self, request, idaluno, idatributo, format=None):
        avaliacao = self.get_object(idaluno, idatributo)
        avaliacao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
