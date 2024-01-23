import requests

# URL base da API
BASE_URL = "http://localhost:8000/api"

# IDs de exemplo para exclusão
aluno_ids = [1, 2, 3, 4, 5]  # Substitua com IDs válidos
fundamento_ids = [1, 2, 3]  # Substitua com IDs válidos
categoria_fundamento_ids = [1, 2]  # Substitua com IDs válidos
avaliacao_ids = [(8, 1), (8, 2), (8, 3)]  # Substitua com combinações válidas de aluno e atributo

# Função para fazer requisições DELETE
def delete_request(url):
    response = requests.delete(url)
    if response.status_code == 204:  # 204 No Content
        print(f"DELETE {url} - Success (204 No Content)")
    elif response.status_code >= 200 and response.status_code < 300:
        # Outros códigos de sucesso que podem conter conteúdo
        print(f"DELETE {url} - Status Code: {response.status_code}, Response: {response.json()}")
    else:
        # Trata todos os outros casos como erro ou resposta sem conteúdo
        print(f"DELETE {url} - Status Code: {response.status_code}, No response content or error occurred")




# Testando exclusão de alunos
for aluno_id in aluno_ids:
    delete_request(f"{BASE_URL}/aluno/{aluno_id}/excluir/")

# Testanto exclusão de atributos
for i in range (1,3):
    delete_request(f"{BASE_URL}/atributo-fundamento/{i}/excluir/")


# Testando exclusão de fundamentos
for fundamento_id in fundamento_ids:
    delete_request(f"{BASE_URL}/fundamento/{fundamento_id}/excluir/")

# Testando exclusão de categorias de fundamentos
for categoria_id in categoria_fundamento_ids:
    delete_request(f"{BASE_URL}/categoria-fundamento/{categoria_id}/excluir/")



# Testando exclusão de avaliações
for aluno_id, atributo_id in avaliacao_ids:
    delete_request(f"{BASE_URL}/avaliacao/{aluno_id}/{atributo_id}/excluir/")

print("Testes de exclusão concluídos.")
