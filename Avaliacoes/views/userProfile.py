from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from ..models import UserProfile
from ..serializers import UserProfileSerializer

class AdicionarUserProfile(APIView):
    def post(self, request, format=None):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalhesUserProfile(APIView):
    def get_object(self, id):
        try:
            return UserProfile.objects.get(id=id)
        except UserProfile.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        userprofile = self.get_object(id)
        serializer = UserProfileSerializer(userprofile)
        return Response(serializer.data)

class EditarUserProfile(APIView):
    def get_object(self, id):
        try:
            return UserProfile.objects.get(id=id)
        except UserProfile.DoesNotExist:
            raise Http404

    def put(self, request, id, format=None):
        userprofile = self.get_object(id)
        serializer = UserProfileSerializer(userprofile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExcluirUserProfile(APIView):
    def get_object(self, id):
        try:
            return UserProfile.objects.get(id=id)
        except UserProfile.DoesNotExist:
            raise Http404

    def delete(self, request, id, format=None):
        userprofile = self.get_object(id)
        userprofile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
