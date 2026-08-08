# Estrutura de permissões

O sistema usa o mecanismo nativo de **grupos e permissões** do Django para controlar o que cada tipo de usuário pode fazer no admin.

## Grupos

| Grupo | Permissões |
|---|---|
| **Clientes** | Apenas visualização de livros (`view_book`) |
| **Funcionários** | CRUD completo em clientes, livros, gêneros, durações de empréstimo e empréstimos; também pode criar, visualizar e editar usuários (`User`), necessário para vincular login aos clientes |

Ambos os grupos são criados automaticamente via uma *migration* de dados (`RunPython`) na app `setup`, junto com suas respectivas permissões.

!!! note "Por que a app `setup`?"
    A migration de grupos e permissões vive na app `setup`, e não em `core`, já que `core` é reservada ao pacote de configuração do projeto (settings, urls, wsgi/asgi).

## Atribuição de grupos é manual

A entrada de um usuário nos grupos "clientes" ou "funcionários" **não é automatizada por signal** — é feita manualmente pelo superusuário ou por um funcionário, no momento em que o `User` é criado ou editado no admin.

## Login individual por cliente

Cada `Client` é vinculado a um `User` por meio de um `OneToOneField`. Esse `User` é criado pelo funcionário diretamente no admin, permitindo que cada cliente tenha um login próprio (`is_staff=True`, restrito pelo grupo "clientes") para acessar o sistema e visualizar o catálogo de livros.

## Trade-off conhecido

O grupo "funcionários" recebe as permissões `add_user`, `view_user` e `change_user` — necessárias para o fluxo de criação de clientes pelo admin padrão do Django. Isso implica um risco teórico de auto-promoção (um funcionário poderia, em teoria, alterar permissões de outro usuário). Esse é um trade-off aceito conscientemente, dado o escopo do projeto como peça de portfólio.
