from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Avaliacao
from ..serializers import AvaliacaoSerializer

class ListarAvaliacoes(APIView):
    def get(self, request, format=None):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

class AdicionarAvaliacao(APIView):
    def post(self, request, format=None):
        serializer = AvaliacaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalhesAvaliacao(APIView):
    def get_object(self, id):
        try:
            return Avaliacao.objects.get(id=id)
        except Avaliacao.DoesNotExist:
            return None

    def get(self, request, id, format=None):
        avaliacao = self.get_object(id)
        if avaliacao is not None:
            serializer = AvaliacaoSerializer(avaliacao)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id, format=None):
        avaliacao = self.get_object(id)
        if avaliacao is not None:
            serializer = AvaliacaoSerializer(avaliacao, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id, format=None):
        avaliacao = self.get_object(id)
        if avaliacao is not None:
            avaliacao.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
