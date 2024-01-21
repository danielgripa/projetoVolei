"""
URL configuration for projetoVolei project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from Avaliacoes.views import alunos,avaliacoes,fundamentos,categoriasFundamento


urlpatterns = [
    #alunos
    path('api/alunos/', alunos.ListarAlunos.as_view(), name='listar_alunos'),
    path('api/alunos/adicionar/', alunos.AdicionarAluno.as_view(), name='adicionar_aluno'),
    path('api/alunos/<int:id>/', alunos.DetalhesAluno.as_view(), name='detalhes_aluno'),
    
    #avaliacoes
    path('api/avaliacoes/', avaliacoes.ListarAvaliacoes.as_view(), name='listar_avaliacoes'),
    path('api/avaliacoes/adicionar/', avaliacoes.AdicionarAvaliacao.as_view(), name='adicionar_avaliacao'),
    path('api/avaliacoes/<int:id>/', avaliacoes.DetalhesAvaliacao.as_view(), name='detalhes_avaliacao'),

    #fundamentos
    path('api/fundamentos/', fundamentos.ListarFundamentos.as_view(), name='listar_fundamentos'),
    path('api/fundamentos/adicionar/', fundamentos.AdicionarFundamento.as_view(), name='adicionar_fundamento'),
    path('api/fundamentos/<int:id>/', fundamentos.DetalhesFundamento.as_view(), name='detalhes_fundamento'),
    
    #categoriaFundamentos
    path('api/categorias-fundamento/', categoriasFundamento.ListarCategoriasFundamento.as_view(), name='listar_categorias_fundamento'),
    path('api/categorias-fundamento/adicionar/', categoriasFundamento.AdicionarCategoriaFundamento.as_view(), name='adicionar_categoria_fundamento'),
    path('api/categorias-fundamento/<int:id>/', categoriasFundamento.DetalhesCategoriaFundamento.as_view(), name='detalhes_categoria_fundamento'),       
]

