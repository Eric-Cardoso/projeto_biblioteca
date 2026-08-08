# Configurando o banco de dados

O projeto usa **SQLite** como banco de dados, sem necessidade de configuração adicional além de aplicar as migrations.

## Aplicando as migrations

```bash
python manage.py migrate
```

Isso cria todas as tabelas do projeto e executa uma *migration* de dados que configura os grupos de permissão iniciais:

- **clientes** — grupo com permissão apenas de visualização de livros
- **funcionários** — grupo com permissão de CRUD completo sobre clientes, livros, gêneros, durações de empréstimo e empréstimos, além de permissão para criar e gerenciar usuários (`User`)

Veja mais detalhes em **[Estrutura de permissões](../uso/permissoes.md)**.

## Criando um superusuário

Para acessar o admin com acesso total, crie um superusuário:

```bash
python manage.py createsuperuser
```

O superusuário não pertence a nenhum dos grupos acima — ele tem acesso irrestrito por definição do Django, e é normalmente quem atribui os grupos "clientes" e "funcionários" aos demais usuários.

Com o banco configurado, siga para **[Uso → Django Admin](../uso/admin.md)**.
