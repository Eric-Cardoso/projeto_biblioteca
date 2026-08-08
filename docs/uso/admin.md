# Django Admin

Toda a interação com o sistema acontece pelo **Django Admin**, personalizado com o pacote **Jazzmin**. Não há views ou templates customizados — essa é uma decisão consciente de escopo do projeto.

## Subindo o servidor

```bash
python manage.py runserver
```

Acesse `http://127.0.0.1:8000` e faça login com o superusuário criado na etapa de **[configuração do banco de dados](../primeiros-passos/configuracao-banco.md)**.

## Personalização visual

O admin foi customizado através de `JAZZMIN_SETTINGS`, incluindo:

- Logo própria do projeto (uma coruja, com o lema "Descobrir · Aprender · Crescer")
- Tela de login personalizada, com o mesmo tema visual do restante do admin
- Ícones específicos por model (Font Awesome), facilitando a navegação visual entre `Client`, `Book`, `Loan`, etc.
- Menu superior com atalhos diretos para os apps `book`, `loan` e `client`

## Fluxo típico de uso

1. O funcionário cria um `User` para o novo cliente pelo admin.
2. Cria o `Client` correspondente, vinculando-o a esse `User`.
3. Atribui manualmente os grupos "clientes" e/ou "funcionários" ao usuário (veja **[Estrutura de permissões](permissoes.md)**).
4. Cadastra livros e gêneros conforme necessário.
5. Registra empréstimos (`Loan`), vinculando cliente, livro e duração de empréstimo.

Ao salvar um empréstimo, o livro correspondente é marcado automaticamente como emprestado — veja como isso funciona em **[Arquitetura → Signals](../arquitetura/signals.md)**.
