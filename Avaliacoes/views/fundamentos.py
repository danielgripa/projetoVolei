from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Fundamento
from ..serializers import FundamentoSerializer
from django.http import Http404

class ListarFundamentos(APIView):
    def get(self, request, format=None):
        fundamentos = Fundamento.objects.all()
        serializer = FundamentoSerializer(fundamentos, many=True)
        return Response(serializer.data)

class AdicionarFundamento(APIView):
    def post(self, request, format=None):
        serializer = FundamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditarFundamento(APIView):
    def get_object(self, id):
        try:
            return Fundamento.objects.get(pk=id)
        except Fundamento.DoesNotExist:
            raise Http404

    def put(self, request, id, format=None):
        fundamento = self.get_object(id)
        serializer = FundamentoSerializer(fundamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExcluirFundamento(APIView):
    def get_object(self, id):
        try:
            return Fundamento.objects.get(pk=id)
        except Fundamento.DoesNotExist:
            raise Http404

    def delete(self, request, id, format=None):
        fundamento = self.get_object(id)
        fundamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class DetalhesFundamento(APIView):
    def get_object(self, id):
        try:
            return Fundamento.objects.get(pk=id)
        except Fundamento.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        fundamento= self.get_object(id)
        serializer = FundamentoSerializer(fundamento)
        return Response(serializer.data)