# Avaliacoes/serializers.py

from rest_framework import serializers
from .models import Aluno, Fundamento, CategoriaFundamento, Avaliacao, AtributoFundamento

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
