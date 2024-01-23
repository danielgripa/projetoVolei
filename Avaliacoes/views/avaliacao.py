from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from ..models import Avaliacao, Aluno, AtributoFundamento
from ..serializers import AvaliacaoSerializer

class RatingAlunoBaseView(APIView):
    """
    Classe base para views de RatingAluno.
    Contém métodos comuns para validação e recuperação de objetos.
    """
    def validate_and_get_aluno(self, idAluno):
        try:
            return Aluno.objects.get(pk=idAluno)
        except Aluno.DoesNotExist:
            raise Http404("Aluno não encontrado.")

    def validate_and_get_atributo(self, idAtributo):
        try:
            return AtributoFundamento.objects.get(pk=idAtributo)
        except AtributoFundamento.DoesNotExist:
            raise Http404("Atributo de Fundamento não encontrado.")

    def get_ratingaluno(self, idAluno, idAtributo):
        try:
            return Avaliacao.objects.get(idAluno=idAluno, idatributo=idAtributo)
        except Avaliacao.DoesNotExist:
            raise Http404("Avaliação de Aluno não encontrada.")

class AdicionarAvaliacao(RatingAlunoBaseView):
    def post(self, request, format=None):
        self.validate_and_get_aluno(request.data.get('idAluno'))
        self.validate_and_get_atributo(request.data.get('idAtributo'))

        serializer = AvaliacaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListarAvaliacoes(RatingAlunoBaseView):
    def get(self, request, format=None):
        ratingalunos = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(ratingalunos, many=True)
        return Response(serializer.data)

class DetalhesAvaliacao(RatingAlunoBaseView):
    def get(self, request, idAluno, idAtributo, format=None):
        ratingaluno = self.get_ratingaluno(idAluno, idAtributo)
        serializer = AvaliacaoSerializer(ratingaluno)
        return Response(serializer.data)

class EditarAvaliacao(RatingAlunoBaseView):
    def put(self, request, idAluno, idAtributo, format=None):
        ratingaluno = self.get_ratingaluno(idAluno, idAtributo)
        serializer = AvaliacaoSerializer(ratingaluno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExcluirAvaliacao(RatingAlunoBaseView):
    def delete(self, request, idAluno, idAtributo, format=None):
        ratingaluno = self.get_ratingaluno(idAluno, idAtributo)
        ratingaluno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
