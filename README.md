# API_Biblioteca
API criada com Django e Rest Framework para um sistema de bibliotecas.


#### 1. Modelagem de Dados

Os seguintes modelos de dados foram implementados para representar o sistema de bibliotecas:

- Livro: Título, Autor, Categoria, Data de Publicação.
- Leitor: Nome, Idade, Cidade
- Empréstimo: Livro, Data de Empréstimo, Data de Devolução, Usuário.

#### 2. Serializers

Foram criados serializers para cada modelo criado. 

#### 3. Autenticação e Permissões

Autenticação por token para API. Com os seguintes grupos de permissões:

- Grupo "Admin": Acesso total para administradores.
- Grupo "Usuários": Acesso para listar e pegar detalhes de livros, autores e empréstimos.
- Grupo "Bibliotecários": Acesso para listar, criar, atualizar e excluir livros, autores e empréstimos.

#### 4. Endpoints e Views

Foram criados os seguintes endpoints e suas respectivas views:

- `/livros/`: Listagem de todos os livros. (GET)
- `/livros/<id>/`: Detalhes de um livro específico. (GET)
- `/leitores/`: Listagem de todos os leitores. (GET)
- `/leitores/<id>/`: Detalhes de um leitor específico. (GET)
- `/emprestimos/`: Listagem de todos os empréstimos. (GET, POST)
- `/emprestimos/<id>/`: Detalhes dos emprestimos