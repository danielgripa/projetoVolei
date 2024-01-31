# Avaliacoes/serializers.py

from rest_framework import serializers
from .models import Aluno, Professor, Fundamento, CategoriaFundamento, Avaliacao, AtributoFundamento, UserProfile, Escola, Quadra, Turma, Aula
from django.contrib.auth.models import User

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'  # Ou especifique os campos que você deseja incluir

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor 
        fields = '__all__'  # Ou especifique os campos que você deseja incluir

class FundamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fundamento
        fields = '__all__'  # Ou especifique os campos que você deseja incluir

class CategoriaFundamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaFundamento
        fields = '__all__'  # Ou especifique os campos que você deseja incluir

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = '__all__'  # Ou especifique os campos que você deseja incluir

class AtributoFundamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtributoFundamento
        fields = '__all__'  # Ou especifique os campos que você deseja incluir

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['is_professor']
        

class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'userprofile']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('userprofile')
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user, **profile_data)
        return user

class EscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escola
        fields = '__all__'  # Ou especifique os campos que você deseja incluir

class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'  # Ou especifique os campos que você deseja incluir

class QuadraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quadra
        fields = '__all__'  # Ou especifique os campos que você deseja incluir

class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = '__all__'  # Ou especifique os campos que você deseja incluir