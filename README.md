# Relatório de Atividade Prática 2 - APPOO

**Instituição:** Universidade Federal de Minas Gerais (UFMG)  
**Disciplina:** Algoritmos e Estruturas de Dados / Programação Orientada a Objetos  
**Professor(a):** Luiza Bernardes Real  
**Ano/Semestre:** 2026/1

## 👥 Alunos Participantes
* **Rafael Campello** (Matrícula: 2024017457)
* **Gustavo Silvestre** (Matrícula: 2024019948)
* **Gustavo de Oliveira Cardoso Rezende** (Matrícula: 2024015802)

## 📝 Descrição da Prática
O objetivo principal deste projeto foi projetar e implementar um sistema orientado a objetos em Python para automatizar o controle de empréstimos de materiais em uma biblioteca. O sistema substitui o antigo registro manual, eliminando problemas de duplicidade de dados e garantindo a integridade das informações cadastradas.

Nesta versão atualizada, a arquitetura foi otimizada para utilizar funções independentes e um controle rigoroso de dados através de encapsulamento, garantindo que valores inválidos não sejam inseridos no sistema, além de possibilitar a persistência dos dados em arquivos de texto (`.txt`).

## 🚀 Destaques e Nova Arquitetura
* **Encapsulamento Robusto com `@property`:** Implementação de métodos *getter* e *setter* para proteger os atributos das classes. O sistema bloqueia ativamente a inserção de usuários ou títulos vazios e garante que os tipos de dados (como datas) estejam estritamente corretos.
* **Arquitetura Orientada a Objetos:** Uso da classe abstrata `Emprestimo` como molde fundamental.
* **Herança e Polimorfismo:** A subclasse `EmprestimoRevista` herda de `EmprestimoLivro`, reaproveitando código e adaptando regras de negócio exclusivas para periódicos.
* **Simplificação e Modularidade:** Substituição de uma classe monolítica de gerenciamento por funções modulares (`listar_emprestimos`, `extrair_dados_texto`, `salvar_em_txt`) que operam diretamente sobre a estrutura de dados global, tornando o script mais limpo e direto.
* **Regras de Negócio Automatizadas:**
    * **Prazos:** 7 dias para livros e 2 dias para revistas, calculados via `datetime`.
    * **Bloqueio de Duplicidades:** Avaliação de múltiplas condições (usuário, título e edição) antes de permitir a efetivação do registro no banco de dados.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3
* **Bibliotecas Nativas:** * `abc`: Para estruturação de classes e métodos abstratos.
    * `datetime`: Para cálculo automatizado das datas de devolução.

---
*Este projeto foi desenvolvido como parte dos requisitos avaliativos da disciplina de Programação Orientada a Objetos.*