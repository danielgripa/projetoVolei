import requests

# Configuração inicial
BASE_URL = "http://localhost:8000/api/"

# Função para fazer uma requisição POST
def post_request(endpoint, payload):
    response = requests.post(f"{BASE_URL}{endpoint}/", json=payload)
    return response.json()

# Cadastrando alunos
for i in range(1, 11):
    aluno_payload = {
        "nomealuno": f"Aluno {i}",
        "datainiciotreino": "2024-01-01",
        "situacaocadastro": "ativo"
    }
    post_request("aluno/adicionar", aluno_payload)

# Cadastrando categorias de fundamentos
for i in range(1, 3):
    categoria_payload = {
        "desc_categoriafundamento": f"Categoria {i}"
    }
    post_request("categoria-fundamento/adicionar", categoria_payload)

# Cadastrando fundamentos
for i in range(1, 6):
    fundamento_payload = {
        "desc_fundamento": f"Fundamento {i}",
        "idcategoriafundamento": 1 if i <= 3 else 2
    }
    post_request("fundamento/adicionar", fundamento_payload)

# Cadastrando atributos
for i in range(1, 6):
    atributo_payload = {
        "idatributo": i,
        "desc_atributofundamento": f"Atributo {i}",
        "fk_idfundamento": i
    }
    post_request("atributo-fundamento/adicionar", atributo_payload)

# Cadastrando avaliações
for aluno_id in range(1, 11):
    for atributo_id in range(1, 6):
        avaliacao_payload = {
            "idaluno": aluno_id,
            "idatributo": atributo_id,
            "score": 8  # Exemplo de score fixo
        }
        post_request("avaliacao/adicionar", avaliacao_payload)

print("Testes finalizados.")
