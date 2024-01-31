from django.db import models
from django.contrib.auth.models import User



class Aluno(models.Model):
    #Associando como usuario do app
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    #Cammpos da tabela
    datainiciotreino = models.DateField(db_column='dataInicioTreino', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'aluno'


class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # Outros campos específicos de professor

    class Meta:
        managed = True
        db_table = 'professor'



class AtributoFundamento(models.Model):
    fk_idfundamento = models.ForeignKey('Fundamento', models.SET_NULL, db_column='fk_idFundamento', blank=True, null=True)  # Field name made lowercase.
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


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_professor = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    
class Escola(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField()

    def __str__(self):
        return self.nome

class Quadra(models.Model):
    identificacao = models.CharField(max_length=100)
    escola = models.ForeignKey(Escola, related_name='quadras', on_delete=models.CASCADE)

    def __str__(self):
        return self.identificacao

class Turma(models.Model):
    descricao = models.CharField(max_length=200)
    professores = models.ManyToManyField(User, related_name='turmas')
    alunos = models.ManyToManyField(User, related_name='turmas_aluno')
    quadra = models.ForeignKey(Quadra, related_name='turmas', on_delete=models.SET_NULL, null=True)
    escola = models.ForeignKey(Escola, related_name='turmas', on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

class Aula(models.Model):
    turma = models.ForeignKey(Turma, related_name='aulas', on_delete=models.CASCADE)
    quadra = models.ForeignKey(Quadra, related_name='aulas', on_delete=models.CASCADE)
    escola = models.ForeignKey(Escola, related_name='aulas', on_delete=models.CASCADE)
    data = models.DateField()
    horario_inicio = models.TimeField()
    duracao = models.DurationField()

    def __str__(self):
        return f"{self.turma} - {self.data} - {self.horario_inicio}"
    

