# book

Responsável pelo catálogo de livros e seus gêneros literários.

## Model `BookGenre`

| Campo | Tipo | Observações |
|---|---|---|
| `name` | texto | Nome do gênero |
| `description` | texto, opcional | Descrição do gênero |

## Model `Book`

| Campo | Tipo | Observações |
|---|---|---|
| `name` | texto | Título do livro |
| `author` | texto | Autor do livro |
| `genre` | `ForeignKey(BookGenre)` | Gênero do livro |
| `isbn` | texto | `unique=True` |
| `was_loaned` | booleano | Atualizado automaticamente via signal ao registrar um empréstimo |
| `description` | texto, opcional | Sinopse ou descrição |
| `publication_date` | data | Data de publicação |

## Signals

`book/signals.py` conecta um receiver que reage ao `post_save` de `Loan`, marcando `was_loaned=True` no `Book` correspondente. Veja **[Signals](../arquitetura/signals.md)**.
