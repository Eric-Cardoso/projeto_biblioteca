# setup

App dedicada exclusivamente a *migrations* de dados — não possui models próprios.

## Migration de grupos e permissões

Usando `migrations.RunPython`, essa app define, na primeira execução de `migrate`:

- O grupo **clientes**, com a permissão `view_book`.
- O grupo **funcionários**, com permissões de `add`, `view` e `change` sobre `User`, `Client`, `BookGenre`, `Book`, `LoanDuration` e `Loan`, além de `delete_loan`.

```python
def define_perm_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    ...
    client_group, _ = Group.objects.get_or_create(name='clientes')
    client_group.permissions.set([perm_view_book])

    employee_group, _ = Group.objects.get_or_create(name='funcionários')
    employee_group.permissions.set([...])
```

A migration também define a operação reversa (`remove_perm_groups`), que remove os dois grupos caso a migration seja revertida.

## Por que uma app separada?

A migration não vive em `core` porque `core` é reservada à configuração do projeto (settings, urls, wsgi/asgi). Uma app dedicada (`setup`) deixa explícito que essa migration existe apenas para popular dados iniciais, sem misturar responsabilidades com nenhum domínio (`client`, `book`, `loan`).
