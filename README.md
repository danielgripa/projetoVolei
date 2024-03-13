# Projeto de Sistema de Avaliação de Vôlei

Este projeto é um sistema de gestão e avaliação para jogadores e treinadores de vôlei, desenvolvido com o objetivo de praticar e demonstrar habilidades em desenvolvimento full-stack, utilizando Django para o back-end e planejando o uso de [React/Angular/Vue] para o front-end.

## Funcionalidades

- **Gerenciamento de Usuários**: Registro e autenticação de usuários, com perfis diferenciados para alunos e professores.
- **Avaliações**: Professores podem criar, editar e remover avaliações dos alunos.
- **Consulta de Avaliações**: Alunos podem consultar apenas suas próprias avaliações.
- **Gestão de Escolas, Turmas, Aulas e Quadras**: Possibilidade de criar e gerenciar escolas, turmas, aulas e quadras relacionadas às sessões de treinamento.

## Tecnologias Utilizadas

- **Back-end**: Django
- **Front-end**: [React/Angular/Vue] (Planejado)
- **Banco de Dados**: MySQL
- **Hospedagem**: AWS (Planejado)

## Aprendizados com o Projeto

Este projeto me proporcionou a oportunidade de aprofundar meus conhecimentos em várias áreas, incluindo:

- Desenvolvimento de API REST com Django Rest Framework.
- Práticas de autenticação e autorização.
- Modelagem e gerenciamento de banco de dados relacional.
- Planejamento e implementação de uma aplicação full-stack.

## Próximos Passos

- [ ] Hospedar a aplicação na AWS.
- [ ] Desenvolver o front-end utilizando [React/Angular/Vue].
- [ ] Implementar funcionalidades adicionais baseadas em feedback dos usuários.


## Como Rodar o Projeto

> Nota: Este guia assume que você tem Python e Django instalados em seu ambiente.

1. Clone o repositório:
git clone https://github.com/danielgripa/projetoVolei.git

2. Instale as dependências:
pip install -r requirements.txt

3. Migre o banco de dados:
python manage.py migrate

4. Inicie o servidor:
python manage.py runserver

## Contribuições

Contribuições são sempre bem-vindas! Por favor, sinta-se à vontade para enviar um pull request ou abrir uma issue para discutir o que você gostaria de mudar.

## Licença

[MIT](LICENSE)

