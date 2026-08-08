# Signals

O projeto usa *signals* do Django para automatizar regras de negócio que devem valer sempre, independente de quem cadastra o quê pelo admin.

## `post_save` em `Client`

Ao salvar um novo `Client`, um signal calcula automaticamente o campo `expiration_date`, definindo-o como **um ano após `issue_date`**. Isso evita que o funcionário precise calcular e preencher essa data manualmente a cada novo cadastro.

## `post_save` em `Loan`

Ao registrar um novo `Loan`, um signal atualiza o campo `was_loaned` do `Book` correspondente para `True`, marcando o livro como emprestado automaticamente — sem precisar de uma ação manual adicional no cadastro do livro.

## O que **não** é feito via signal

A atribuição de grupos de permissão ("clientes" e "funcionários") a um `User` **não** é automatizada por signal — é feita manualmente pelo funcionário ou superusuário no admin. Veja **[Estrutura de permissões](../uso/permissoes.md)** para mais detalhes sobre esse fluxo.

## Registrando os signals

Os signals de cada app são conectados no método `ready()` da respectiva `AppConfig`, importando o módulo `signals` (com `# noqa: F401`, já que o import existe pelo efeito colateral de registrar os receivers, não para uso direto):

```python
def ready(self):
    from . import signals  # noqa: F401
```
