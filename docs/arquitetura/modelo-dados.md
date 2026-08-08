# Modelo de dados

```mermaid
erDiagram
    USER ||--o| CLIENT : "possui login"
    CLIENT ||--o{ LOAN : realiza
    BOOK ||--o{ LOAN : "é emprestado em"
    BOOKGENRE ||--o{ BOOK : classifica
    LOANDURATION ||--o{ LOAN : define

    USER {
        int id PK
    }
    CLIENT {
        int id PK
        int user FK
        text name
        text cpf
        text phone
        date issue_date
        date expiration_date
    }
    BOOK {
        int id PK
        text name
        text author
        int genre FK
        text isbn
        boolean was_loaned
        text description
        date publication_date
    }
    BOOKGENRE {
        int id PK
        text name
        text description
    }
    LOANDURATION {
        int id PK
        text name
        text description
    }
    LOAN {
        int id PK
        int client FK
        int book FK
        date loan_date
        int loan_duration FK
        date devolution_date
    }
```

## Notas sobre os campos

- **`Client.expiration_date`** — calculado automaticamente como um ano após `issue_date`. Veja **[Signals](signals.md)**.
- **`Book.isbn`** — possui `unique=True`, garantindo que não existam livros duplicados por ISBN.
- **`Book.was_loaned`** — atualizado automaticamente via signal ao registrar um `Loan` para aquele livro.
- **`Loan`** — todas as *foreign keys* (`client`, `book`, `loan_duration`) usam `on_delete=PROTECT`, impedindo a exclusão de clientes, livros ou durações que já têm empréstimos associados.
