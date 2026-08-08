# Configuração do projeto

Metadados e ferramentas do projeto são definidos em `pyproject.toml`.

```toml
[project]
name = 'projeto-biblioteca'
version = '0.1.0'
requires-python = '>=3.12'
description = '''
Sistema de gestão de biblioteca construído com Django, focado no cadastro
de clientes, livros e no controle de empréstimos, do início ao fim, direto
pelo Django Admin. Permite gerenciar clientes, livros, gêneros literários,
durações de empréstimo e empréstimos, com automações via signals e
controle de permissões por grupo (clientes e funcionários). Desenvolvido
com django-environ para configuração via variáveis de ambiente e Jazzmin
para personalização visual do admin.
'''
authors = [
    {name = 'Eric', email = 'ericcardoso454@gmail.com'}
]

[tool.black]
line-length = 88
skip-string-normalization = true

[tool.isort]
profile = "black"
line_length = 88
```

## Dependências principais

| Pacote | Papel |
|---|---|
| `Django` | Framework web |
| `django-environ` | Carregamento de configuração via `.env` |
| `django-jazzmin` | Personalização visual do Django Admin |

## Dependências de qualidade e documentação

| Pacote | Papel |
|---|---|
| `black`, `isort`, `flake8` | Formatação e *linting* — veja **[Qualidade de código](qualidade-codigo.md)** |
| `mkdocs` | Geração desta documentação |

Todas as versões exatas estão fixadas em `requirements.txt`.
