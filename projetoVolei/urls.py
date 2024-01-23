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
from Avaliacoes.views import alunos, avaliacao,fundamentos,categoriasFundamento, atributoFundamento


urlpatterns = [
    # Alunos
    path('api/aluno/', alunos.ListarAlunos.as_view(), name='listar_alunos'),
    path('api/aluno/adicionar/', alunos.AdicionarAluno.as_view(), name='adicionar_aluno'),
    path('api/aluno/<int:id>/', alunos.DetalhesAluno.as_view(), name='detalhes_aluno'),
    path('api/aluno/<int:id>/excluir/', alunos.ExcluirAluno.as_view(), name="excluir_aluno"),
    path('api/aluno/<int:id>/editar/', alunos.EditarAluno.as_view(), name="editar_aluno"),

    # Avaliações
    path('api/avaliacao/', avaliacao.ListarAvaliacoes.as_view(), name='listar_avaliacoes'),
    path('api/avaliacao/adicionar/', avaliacao.AdicionarAvaliacao.as_view(), name='adicionar_avaliacao'),
    path('api/avaliacao/<int:id>/', avaliacao.DetalhesAvaliacao.as_view(), name='detalhes_avaliacao'),
    path('api/avaliacao/<int:idaluno>/<int:idatributo>/excluir/', avaliacao.ExcluirAvaliacao.as_view(), name="excluir_avaliacao"),
    path('api/avaliacao/<int:idaluno>/<int:idatributo>/editar/', avaliacao.EditarAvaliacao.as_view(), name="editar_avaliacao"),
    
    # Fundamentos
    path('api/fundamento/', fundamentos.ListarFundamentos.as_view(), name='listar_fundamentos'),
    path('api/fundamento/adicionar/', fundamentos.AdicionarFundamento.as_view(), name='adicionar_fundamento'),
    path('api/fundamento/<int:id>/', fundamentos.DetalhesFundamento.as_view(), name='detalhes_fundamento'),
    path('api/fundamento/<int:id>/excluir/', fundamentos.ExcluirFundamento.as_view(), name="excluir_fundamento"),
    path('api/fundamento/<int:id>/editar/', fundamentos.EditarFundamento.as_view(), name="editar_fundamento"),

    # CategoriaFundamentos
    path('api/categoria-fundamento/', categoriasFundamento.ListarCategoriasFundamento.as_view(), name='listar_categorias_fundamento'),
    path('api/categoria-fundamento/adicionar/', categoriasFundamento.AdicionarCategoriaFundamento.as_view(), name='adicionar_categoria_fundamento'),
    path('api/categoria-fundamento/<int:id>/', categoriasFundamento.DetalhesCategoriaFundamento.as_view(), name='detalhes_categoria_fundamento'),       
    path('api/categoria-fundamento/<int:id>/excluir/', categoriasFundamento.ExcluirCategoriaFundamento.as_view(), name="excluir_categoria_fundamento"),
    path('api/categoria-fundamento/<int:id>/editar/', categoriasFundamento.EditarCategoriaFundamento.as_view(), name="editar_categoria_fundamento"),

    # AtributoFundamento
    path('api/atributo-fundamento/', atributoFundamento.ListarAtributos.as_view(), name='listar_atributo_fundamento'),
    path('api/atributo-fundamento/adicionar/', atributoFundamento.AdicionarAtributo.as_view(), name='adicionar_atributo_fundamento'),
    path('api/atributo-fundamento/<int:id>/', atributoFundamento.DetalhesAtributo.as_view(), name='detalhes_atributo_fundamento'),       
    path('api/atributo-fundamento/<int:id>/excluir/', atributoFundamento.ExcluirAtributo.as_view(), name='excluir_atributo_fundamento'),
    path('api/atributo-fundamento/<int:id>/editar/', atributoFundamento.EditarAtributo.as_view(), name='editar_atributo_fundamento'),
]
