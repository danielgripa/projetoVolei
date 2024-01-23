from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import AtributoFundamento
from ..serializers import AtributoFundamentoSerializer
from django.http import Http404

class AdicionarAtributo(APIView):
    def post(self, request, format=None):
        serializer = AtributoFundamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListarAtributos(APIView):
    def get(self, request, format=None):
        atributos = AtributoFundamento.objects.all()
        serializer = AtributoFundamentoSerializer(atributos, many=True)
        return Response(serializer.data)

class DetalhesAtributo(APIView):
    def get_object(self, id):
        try:
            return AtributoFundamento.objects.get(pk=id)
        except AtributoFundamento.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        atributo = self.get_object(id)
        serializer = AtributoFundamentoSerializer(atributo)
        return Response(serializer.data)

class EditarAtributo(APIView):
    def get_object(self, id):
        try:
            return AtributoFundamento.objects.get(pk=id)
        except AtributoFundamento.DoesNotExist:
            raise Http404

    def put(self, request, id, format=None):
        atributo = self.get_object(id)
        serializer = AtributoFundamentoSerializer(atributo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExcluirAtributo(APIView):
    def get_object(self, id):
        try:
            return AtributoFundamento.objects.get(pk=id)
        except AtributoFundamento.DoesNotExist:
            raise Http404

    def delete(self, request, id, format=None):
        atributo = self.get_object(id)
        atributo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
