# Qualidade de código

O projeto usa três ferramentas complementares para manter o código consistente: **isort**, **black** e **flake8**, sempre executadas nessa ordem.

```bash
isort .
black .
flake8
```

| Ferramenta | Papel |
|---|---|
| `isort` | Organiza e ordena os imports |
| `black` | Formata o código automaticamente para um padrão consistente |
| `flake8` | Faz o *linting*: aponta problemas de estilo, imports não usados e más práticas — não corrige nada, só avisa |

## Configuração

As três ferramentas são configuradas no `pyproject.toml` e no `.flake8`:

```toml
[tool.black]
line-length = 88
skip-string-normalization = true

[tool.isort]
profile = "black"
line_length = 88
```

```ini
[flake8]
max-line-length = 88
extend-ignore = E203, W503
exclude = venv, */migrations/*
```

`E203` e `W503` são ignoradas por conflitarem com o estilo de formatação do `black`. O diretório `venv` e as pastas `migrations` são excluídas da análise do `flake8`, já que contêm código de terceiros e código gerado automaticamente, respectivamente.

## Exceções pontuais

Em alguns casos, um `# noqa` é usado para sinalizar ao `flake8` que uma linha específica é intencional — por exemplo, o import de `signals` dentro de `ready()`, que existe pelo efeito colateral de registrar os receivers, não para uso direto:

```python
def ready(self):
    from . import signals  # noqa: F401
```
