from django.db import models


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


# Create your models here.
class Aluno(models.Model):
    idaluno = models.AutoField(db_column='idAluno', primary_key=True)  # Field name made lowercase.
    nomealuno = models.CharField(db_column='nomeAluno', max_length=255)  # Field name made lowercase.
    datainiciotreino = models.DateField(db_column='dataInicioTreino', blank=True, null=True)  # Field name made lowercase.
    situacaocadastro = models.CharField(db_column='situacaoCadastro', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aluno'


class Categoriafundamento(models.Model):
    idcategoriafundamento = models.AutoField(db_column='idCategoriaFundamento', primary_key=True)  # Field name made lowercase.
    desc_categoriafundamento = models.CharField(db_column='desc_categoriaFundamento', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categoriaFundamento'


class Fundamento(models.Model):
    idfundamento = models.AutoField(db_column='idFundamento', primary_key=True)  # Field name made lowercase.
    desc_fundamento = models.CharField(db_column='desc_Fundamento', max_length=255)  # Field name made lowercase.
    idcategoriafundamento = models.ForeignKey(Categoriafundamento, models.DO_NOTHING, db_column='idCategoriaFundamento', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fundamento'


class Ratingaluno(models.Model):
    idaluno = models.ForeignKey(Aluno, models.CASCADE, db_column='idAluno', blank=True, null=True)  # Field name made lowercase.
    idfundamento = models.ForeignKey(Fundamento, models.DO_NOTHING, db_column='idFundamento', blank=True, null=True)  # Field name made lowercase.
    idatributo = models.IntegerField(db_column='idAtributo', blank=True, null=True)  # Field name made lowercase.
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ratingAluno'
