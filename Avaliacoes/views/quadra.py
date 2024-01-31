from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Quadra
from ..serializers import QuadraSerializer
from django.http import Http404
from django.shortcuts import get_object_or_404


class ListarQuadras(APIView):
    def get(self, request, format=None):
        quadras = Quadra.objects.all()
        serializer = QuadraSerializer(quadras, many=True)
        return Response(serializer.data)

class DetalhesQuadra(APIView):
    def get_object(self, id):
        try:
            return Quadra.objects.get(pk=id)
        except Quadra.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        quadra = self.get_object(id)
        serializer = QuadraSerializer(quadra)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        quadra = self.get_object(id)
        serializer = QuadraSerializer(quadra, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        quadra = self.get_object(id)
        quadra.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AdicionarQuadra(APIView):
    def post(self, request, format=None):
        serializer = QuadraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditarQuadra(APIView):
    def put(self, request, id, format=None):
        quadra = get_object_or_404(Quadra, pk=id)
        serializer = QuadraSerializer(quadra, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExcluirQuadra(APIView):
    def delete(self, request, id, format=None):
        quadra = get_object_or_404(Quadra, pk=id)
        quadra.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)