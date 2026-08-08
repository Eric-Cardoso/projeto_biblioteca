# Configuração

O projeto usa **django-environ** para carregar configurações sensíveis a partir de um arquivo `.env`, mantendo `SECRET_KEY`, `DEBUG` e `ALLOWED_HOSTS` fora do código versionado.

## Criando o `.env`

Copie o arquivo de exemplo:

```bash
cp .env-example .env
```

E preencha as variáveis:

```dotenv
SECRET_KEY=
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

| Variável | Descrição |
|---|---|
| `SECRET_KEY` | Chave secreta do Django, usada para assinaturas criptográficas. Gere uma própria, sem aspas nem colchetes no valor. |
| `DEBUG` | Deve ser `True` em desenvolvimento local. |
| `ALLOWED_HOSTS` | Lista de hosts autorizados, separados por vírgula e **sem** porta (ex: `127.0.0.1`, não `127.0.0.1:8000`). |

!!! warning "Mantenha `DEBUG=True` em desenvolvimento"
    Este projeto é destinado a ambiente de desenvolvimento. Com `DEBUG=False`, o Django deixa de servir arquivos estáticos (logo, CSS e JS do admin) automaticamente — a logo do Jazzmin e os ícones do menu somem, e o admin fica visualmente quebrado.

    Para produção, seria necessário configurar um servidor de arquivos estáticos dedicado (ex: **whitenoise** ou **nginx**), o que está fora do escopo deste projeto.

Com o `.env` configurado, siga para **[Configurando o banco de dados](configuracao-banco.md)**.
