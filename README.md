## 📦 Instalação de Pacotes Necessários

Antes de executar o projeto, certifique-se de que você tem o Python instalado. Depois, instale as bibliotecas necessárias com os seguintes comandos:

```bash
pip install flask graphene
pip install flask-graphql



# 📦 API GraphQL com Flask e Graphene

Este projeto é uma API simples feita com **Flask** e **Graphene (GraphQL)** em Python, que simula um banco de dados de produtos e usuários.

---

## 📘 Sintaxe do GraphQL

GraphQL é uma linguagem de consulta para APIs. Diferente do REST, que usa múltiplas rotas, o GraphQL trabalha com apenas **um endpoint** e permite que o cliente defina **exatamente os dados que deseja**.

### 🧩 Tipos de operações

- `query`: Usada para **buscar dados** (sem modificar nada).
- `mutation`: Usada para **criar, atualizar ou excluir** dados.

### 📐 Estrutura geral

```graphql
# Consulta (query)
query {
  nomeDaQuery(argumentos) {
    campo1
    campo2
  }
}

# Mutação (mutation)
mutation {
  nomeDaMutacao(argumentos) {
    nomeDoObjeto {
      campo1
      campo2
    }
  }
}
