# Instalação

## Requisitos

- Python 3.12+

## Passo a passo

Clone o repositório e entre na pasta do projeto:

```bash
git clone <url-do-repositorio>
cd projeto_bibilioteca
```

Crie e ative um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

!!! note "Windows"
```bash
python -m venv venv
venv\Scripts\activate
```

Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

Com o ambiente virtual ativo e as dependências instaladas, siga para **[Configuração](configuracao.md)** para preparar o arquivo `.env`.
