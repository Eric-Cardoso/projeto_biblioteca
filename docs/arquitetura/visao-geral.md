# Visão geral

O projeto é organizado em apps Django, cada uma com uma responsabilidade clara dentro do domínio de biblioteca.

## Apps

| App | Responsabilidade |
|---|---|
| `core` | Configuração do projeto: settings, urls, wsgi/asgi |
| `client` | Cadastro de clientes e vínculo com `User` |
| `book` | Livros e gêneros literários |
| `loan` | Empréstimos e durações de empréstimo |
| `setup` | Migrations de dados (grupos e permissões iniciais) |

## Decisões de design

- **Apenas Django Admin, sem views customizadas.** O projeto usa o admin como interface completa de uso, personalizado com Jazzmin.
- **SQLite como banco de dados.** Suficiente para o escopo do projeto; Postgres/Docker ficam como evolução futura planejada, fora do escopo atual.
- **`on_delete=PROTECT`** em todas as relações de `loan`, para evitar exclusões em cascata que apaguem histórico de empréstimos.
- **Automação via signals** para regras de negócio que devem acontecer sempre, independente de quem interage com o admin (veja **[Signals](signals.md)**).

Para os detalhes de cada tabela e como elas se relacionam, veja **[Modelo de dados](modelo-dados.md)**.
