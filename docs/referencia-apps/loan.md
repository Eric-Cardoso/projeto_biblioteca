# loan

Responsável pelo controle de empréstimos de livros.

## Model `LoanDuration`

| Campo | Tipo | Observações |
|---|---|---|
| `name` | texto | Nome da duração (ex: "7 dias", "15 dias") |
| `description` | texto, opcional | Descrição adicional |

## Model `Loan`

| Campo | Tipo | Observações |
|---|---|---|
| `client` | `ForeignKey(Client)` | `on_delete=PROTECT` |
| `book` | `ForeignKey(Book)` | `on_delete=PROTECT` |
| `loan_date` | data | `auto_now_add=True` |
| `loan_duration` | `ForeignKey(LoanDuration)` | `on_delete=PROTECT` |
| `devolution_date` | data, opcional | Preenchida na devolução |

Todas as *foreign keys* usam `on_delete=PROTECT`, impedindo a exclusão de clientes, livros ou durações que já tenham empréstimos vinculados — preservando o histórico.

## Signals

Ao salvar um `Loan`, um receiver em `book/signals.py` marca o `Book` correspondente como emprestado (`was_loaned=True`). Veja **[Signals](../arquitetura/signals.md)**.
