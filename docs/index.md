# Biblioteca Admin

Sistema de gestão de biblioteca construído com **Django**, focado no cadastro de clientes, livros e no controle de empréstimos — do início ao fim, direto pelo Django Admin.

Permite gerenciar clientes, livros, gêneros literários, durações de empréstimo e empréstimos, com automações via *signals* (status do livro, cálculo de expiração de cadastro) e controle de permissões por grupo (clientes e funcionários).

Desenvolvido com **django-environ** para configuração via variáveis de ambiente e **Jazzmin** para personalização visual do admin.

## Por que este projeto existe

Este projeto foi construído como peça de portfólio, com foco em:

- Modelagem de dados relacional em Django (models, relacionamentos, `on_delete`)
- Automação de regras de negócio via *signals*
- Controle de acesso granular usando grupos e permissões nativas do Django
- Personalização do Django Admin como interface completa de uso, sem views customizadas

!!! info "Escopo consciente"
    O projeto utiliza **apenas o Django Admin** como interface — não há views ou templates customizados. Essa é uma decisão deliberada de escopo, não uma limitação técnica.

## Para onde ir agora

- Nunca rodou o projeto? Comece por **[Primeiros passos → Instalação](primeiros-passos/instalacao.md)**.
- Quer entender como o admin é usado no dia a dia? Veja **[Uso → Django Admin](uso/admin.md)**.
- Curioso sobre a modelagem e as automações? Veja **[Arquitetura → Visão geral](arquitetura/visao-geral.md)**.
