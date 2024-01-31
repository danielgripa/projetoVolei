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
from Avaliacoes.views import user, alunos ,professor, avaliacao, fundamentos, categoriasFundamento, atributoFundamento, userProfile, quadra, aula, turma, escola


urlpatterns = [
    # Usuários
    path('users/', user.ListarUsers.as_view(), name='listar_users'),
    path('users/adicionar/', user.AdicionarUser.as_view(), name='adicionar_user'),
    path('users/<int:id>/', user.DetalhesUser.as_view(), name='detalhes_user'),
    path('users/<int:id>/editar/',user.EditarUser.as_view(), name='editar_user'),
    path('users/<int:id>/excluir/', user.ExcluirUser.as_view(), name='excluir_user'),

    # URLs para UserProfile
    path('userprofiles/adicionar/', userProfile.AdicionarUserProfile.as_view(), name='adicionar_userprofile'),
    path('userprofiles/<int:id>/', userProfile.DetalhesUserProfile.as_view(), name='detalhes_userprofile'),
    path('userprofiles/<int:id>/editar/', userProfile.EditarUserProfile.as_view(), name='editar_userprofile'),
    path('userprofiles/<int:id>/excluir/', userProfile.ExcluirUserProfile.as_view(), name='excluir_userprofile'),

    # Alunos
    path('api/aluno/', alunos.ListarAlunos.as_view(), name='listar_alunos'),
    path('api/aluno/adicionar/', alunos.AdicionarAluno.as_view(), name='adicionar_aluno'),
    path('api/aluno/<int:id>/', alunos.DetalhesAluno.as_view(), name='detalhes_aluno'),
    path('api/aluno/<int:id>/excluir/', alunos.ExcluirAluno.as_view(), name="excluir_aluno"),
    path('api/aluno/<int:id>/editar/', alunos.EditarAluno.as_view(), name="editar_aluno"),

    # Professor
    path('api/professor/', professor.ListarProfessores.as_view(), name='listar_professores'),
    path('api/professor/adicionar/', professor.AdicionarProfessor.as_view(), name='adicionar_professor'),
    path('api/professor/<int:user_id>/', professor.DetalhesProfessor.as_view(), name='detalhes_professor'),
    path('api/professor/<int:user_id>/editar/', professor.EditarProfessor.as_view(), name='editar_professor'),
    path('api/professor/<int:user_id>/excluir/', professor.ExcluirProfessor.as_view(), name='excluir_professor'),

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

    # Escola
    path('escola/', escola.ListarEscolas.as_view(), name='listar_escolas'),
    path('escola/adicionar/', escola.AdicionarEscola.as_view(), name='adicionar_escola'),
    path('escola/<int:id>/', escola.DetalhesEscola.as_view(), name='detalhes_escola'),
    path('escola/<int:id>/editar/', escola.EditarEscola.as_view(), name='editar_escola'),
    path('escola/<int:id>/excluir/', escola.ExcluirEscola.as_view(), name='excluir_escola'),
    
    # Turma
    path('turma/', turma.ListarTurmas.as_view(), name='listar_turmas'),
    path('turma/adicionar/', turma.AdicionarTurma.as_view(), name='adicionar_turma'),
    path('turma/<int:id>/', turma.DetalhesTurma.as_view(), name='detalhes_turma'),
    path('turma/<int:id>/editar/', turma.EditarTurma.as_view(), name='editar_turma'),
    path('turma/<int:id>/excluir/', turma.ExcluirTurma.as_view(), name='excluir_turma'),
    
    # Aula
    path('aula/', aula.ListarAulas.as_view(), name='listar_aulas'),
    path('aula/adicionar/', aula.AdicionarAula.as_view(), name='adicionar_aula'),
    path('aula/<int:id>/', aula.DetalhesAula.as_view(), name='detalhes_aula'),
    path('aula/<int:id>/editar/', aula.EditarAula.as_view(), name='editar_aula'),
    path('aula/<int:id>/excluir/', aula.ExcluirAula.as_view(), name='excluir_aula'),
    
    # Quadra
    path('quadra/', quadra.ListarQuadras.as_view(), name='listar_quadras'),
    path('quadra/adicionar/', quadra.AdicionarQuadra.as_view(), name='adicionar_quadra'),
    path('quadra/<int:id>/', quadra.DetalhesQuadra.as_view(), name='detalhes_quadra'),
    path('quadra/<int:id>/editar/', quadra.EditarQuadra.as_view(), name='editar_quadra'),
    path('quadra/<int:id>/excluir/', quadra.ExcluirQuadra.as_view(), name='excluir_quadra'),
]