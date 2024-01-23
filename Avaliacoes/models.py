from django.db import models


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.



class Aluno(models.Model):
    idaluno = models.AutoField(db_column='idAluno', primary_key=True)  # Field name made lowercase.
    nomealuno = models.CharField(db_column='nomeAluno', max_length=255)  # Field name made lowercase.
    datainiciotreino = models.DateField(db_column='dataInicioTreino', blank=True, null=True)  # Field name made lowercase.
    situacaocadastro = models.CharField(db_column='situacaoCadastro', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'aluno'


class AtributoFundamento(models.Model):
    fk_idfundamento = models.ForeignKey('Fundamento', models.RESTRICT, db_column='fk_idFundamento')  # Field name made lowercase.
    idatributo = models.IntegerField(db_column='idAtributo', primary_key=True)  # Field name made lowercase.
    desc_atributofundamento = models.CharField(db_column='desc_atributoFundamento', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'atributoFundamento'


class CategoriaFundamento(models.Model):
    idcategoriafundamento = models.AutoField(db_column='idCategoriaFundamento', primary_key=True)  # Field name made lowercase.
    desc_categoriafundamento = models.CharField(db_column='desc_categoriaFundamento', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'categoriaFundamento'


class Fundamento(models.Model):
    idfundamento = models.AutoField(db_column='idFundamento', primary_key=True)  # Field name made lowercase.
    desc_fundamento = models.CharField(db_column='desc_Fundamento', max_length=255)  # Field name made lowercase.
    idcategoriafundamento = models.ForeignKey(CategoriaFundamento, models.SET_NULL, db_column='idCategoriaFundamento', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'fundamento'


class Avaliacao(models.Model):
    idaluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, db_column='idAluno')  # ForeignKey para permitir múltiplas avaliações por aluno
    idatributo = models.ForeignKey(AtributoFundamento, on_delete=models.CASCADE, db_column='idAtributo')
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'avaliacao'
        unique_together = (('idaluno', 'idatributo'),)  # Garante a unicidade de cada combinação de aluno e atributo

