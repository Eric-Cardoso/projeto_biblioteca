# client

Responsável pelo cadastro de clientes da biblioteca.

## Model `Client`

| Campo | Tipo | Observações |
|---|---|---|
| `user` | `OneToOneField(User)` | Login individual do cliente |
| `name` | texto | Nome completo |
| `cpf` | texto | Documento do cliente |
| `phone` | texto, opcional | Telefone de contato |
| `issue_date` | data | Data de emissão do cadastro |
| `expiration_date` | data | Calculado automaticamente (`issue_date` + 1 ano) via signal — veja **[Signals](../arquitetura/signals.md)** |

## Signals

`client/signals.py` conecta um receiver de `post_save` que preenche `expiration_date` automaticamente na criação de um novo `Client`.

## Permissões relacionadas

O grupo "clientes" tem apenas `view_book`. O grupo "funcionários" tem CRUD completo sobre `Client`. Veja **[Estrutura de permissões](../uso/permissoes.md)**.
