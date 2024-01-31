# Generated by Django 5.0.1 on 2024-01-31 21:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaFundamento',
            fields=[
                ('idcategoriafundamento', models.AutoField(db_column='idCategoriaFundamento', primary_key=True, serialize=False)),
                ('desc_categoriafundamento', models.CharField(db_column='desc_categoriaFundamento', max_length=255)),
            ],
            options={
                'db_table': 'categoriaFundamento',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Escola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'professor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datainiciotreino', models.DateField(blank=True, db_column='dataInicioTreino', null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'aluno',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Fundamento',
            fields=[
                ('idfundamento', models.AutoField(db_column='idFundamento', primary_key=True, serialize=False)),
                ('desc_fundamento', models.CharField(db_column='desc_Fundamento', max_length=255)),
                ('idcategoriafundamento', models.ForeignKey(blank=True, db_column='idCategoriaFundamento', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Avaliacoes.categoriafundamento')),
            ],
            options={
                'db_table': 'fundamento',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AtributoFundamento',
            fields=[
                ('idatributo', models.IntegerField(db_column='idAtributo', primary_key=True, serialize=False)),
                ('desc_atributofundamento', models.CharField(db_column='desc_atributoFundamento', max_length=45)),
                ('fk_idfundamento', models.ForeignKey(blank=True, db_column='fk_idFundamento', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Avaliacoes.fundamento')),
            ],
            options={
                'db_table': 'atributoFundamento',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Quadra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacao', models.CharField(max_length=100)),
                ('escola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quadras', to='Avaliacoes.escola')),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
                ('alunos', models.ManyToManyField(related_name='turmas_aluno', to=settings.AUTH_USER_MODEL)),
                ('escola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turmas', to='Avaliacoes.escola')),
                ('professores', models.ManyToManyField(related_name='turmas', to=settings.AUTH_USER_MODEL)),
                ('quadra', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='turmas', to='Avaliacoes.quadra')),
            ],
        ),
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('horario_inicio', models.TimeField()),
                ('duracao', models.DurationField()),
                ('escola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aulas', to='Avaliacoes.escola')),
                ('quadra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aulas', to='Avaliacoes.quadra')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aulas', to='Avaliacoes.turma')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_professor', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(blank=True, null=True)),
                ('idaluno', models.ForeignKey(db_column='idAluno', on_delete=django.db.models.deletion.CASCADE, to='Avaliacoes.aluno')),
                ('idatributo', models.ForeignKey(db_column='idAtributo', on_delete=django.db.models.deletion.CASCADE, to='Avaliacoes.atributofundamento')),
            ],
            options={
                'db_table': 'avaliacao',
                'managed': True,
                'unique_together': {('idaluno', 'idatributo')},
            },
        ),
    ]
