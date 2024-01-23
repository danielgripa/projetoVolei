import requests

# URL base da API
BASE_URL = "http://localhost:8000/api"

# IDs de exemplo para edição (substitua por IDs válidos)
aluno_id = 1
fundamento_id = 1
categoria_fundamento_id = 1
avaliacao_id_aluno = 1
avaliacao_id_atributo = 1
atributo_fundamento_id = 1

# Dados de exemplo para edição
novo_nome_aluno = "Nome Alterado"
novo_score_avaliacao = 9
novo_desc_fundamento = "Fundamento Modificado"
novo_desc_categoria_fundamento = "Categoria Modificada"

# Função para fazer requisições PUT
def put_request(url, data):
    response = requests.put(url, json=data)
    try:
        response_data = response.json()
    except ValueError:  # Lidando com respostas sem corpo
        response_data = "No Content"
    print(f"PUT {url} - Status Code: {response.status_code}, Response: {response_data}")

# Editando um aluno (inclua todos os campos obrigatórios)
put_request(f"{BASE_URL}/aluno/{aluno_id}/editar/", {'nomealuno': novo_nome_aluno, 'situacaocadastro': 'ativo'})

# Editando uma avaliação
put_request(f"{BASE_URL}/avaliacao/{avaliacao_id_aluno}/{avaliacao_id_atributo}/editar/", {'idaluno':avaliacao_id_aluno,'idatributo':avaliacao_id_atributo,'score': novo_score_avaliacao})

# Editando um fundamento
put_request(f"{BASE_URL}/fundamento/{fundamento_id}/editar/", {'desc_fundamento': novo_desc_fundamento, 'idcategoriafundamento': 1})

# Editando uma categoria de fundamento
put_request(f"{BASE_URL}/categoria-fundamento/{categoria_fundamento_id}/editar/", {'desc_categoriafundamento': novo_desc_categoria_fundamento})

# Editando um atributo de fundamento
put_request(f"{BASE_URL}/atributo-fundamento/{atributo_fundamento_id}/editar/", {'idatributo': atributo_fundamento_id,'desc_atributofundamento': novo_desc_categoria_fundamento, 'fk_idfundamento': 5})

print("Testes de edição concluídos.")
