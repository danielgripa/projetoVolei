# Avaliacoes/serializers.py

from rest_framework import serializers
from .models import Aluno, Fundamento, Categoriafundamento, Ratingaluno

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'  # Ou especifique os campos que você deseja incluir

class FundamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fundamento
        fields = '__all__'  # Ou especifique os campos que você deseja incluir

class CategoriaFundamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoriafundamento
        fields = '__all__'  # Ou especifique os campos que você deseja incluir

class RatingalunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratingaluno
        fields = '__all__'  # Ou especifique os campos que você deseja incluir
