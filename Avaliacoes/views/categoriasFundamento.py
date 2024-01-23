from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import CategoriaFundamento
from ..serializers import CategoriaFundamentoSerializer
from django.http import Http404

class ListarCategoriasFundamento(APIView):
    def get(self, request, format=None):
        categorias = CategoriaFundamento.objects.all()
        serializer = CategoriaFundamentoSerializer(categorias, many=True)
        return Response(serializer.data)

class AdicionarCategoriaFundamento(APIView):
    def post(self, request, format=None):
        serializer = CategoriaFundamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalhesCategoriaFundamento(APIView):
    def get_object(self, id):
        try:
            return CategoriaFundamento.objects.get(pk=id)
        except CategoriaFundamento.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        categoria = self.get_object(id)
        serializer = CategoriaFundamentoSerializer(categoria)
        return Response(serializer.data)
    

class EditarCategoriaFundamento(APIView):
    def get_object(self, id):
        try:
            return CategoriaFundamento.objects.get(pk=id)
        except CategoriaFundamento.DoesNotExist:
            raise Http404

    def put(self, request, id, format=None):
        categoriafundamento = self.get_object(id)
        serializer = CategoriaFundamentoSerializer(categoriafundamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExcluirCategoriaFundamento(APIView):
    def get_object(self, id):
        try:
            return CategoriaFundamento.objects.get(pk=id)
        except CategoriaFundamento.DoesNotExist:
            raise Http404

    def delete(self, request, id, format=None):
        fundamento = self.get_object(id)
        fundamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
