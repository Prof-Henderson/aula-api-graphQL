# Importa as bibliotecas necessárias do Flask e do Graphene (GraphQL para Python)
from flask import Flask, request, jsonify
import graphene

# Define um modelo GraphQL chamado Produto, com os campos id, nome e preco
class Produto(graphene.ObjectType):
    id = graphene.Int()        # Campo inteiro (ex: 1, 2, 3)
    nome = graphene.String()   # Campo string (ex: "Camiseta")
    preco = graphene.Float()   # Campo float (ex: 50.00)

# Cria uma lista simulando um banco de dados com dois produtos
produtos = [
    {"id": 1, "nome": "Camiseta", "preco": 50.00},
    {"id": 2, "nome": "Tênis", "preco": 120.00}
]

# Define a classe de consultas (queries) da API GraphQL
class Query(graphene.ObjectType):
    # Define uma query que busca um produto pelo ID
    produto = graphene.Field(Produto, id=graphene.Int())
    # Define uma query que retorna a lista de todos os produtos
    produtos = graphene.List(Produto)

    # Função que resolve a query "produto", buscando pelo ID informado
    def resolve_produto(root, info, id):
        return next((p for p in produtos if p['id'] == id), None)  # Retorna o primeiro produto com ID correspondente

    # Função que resolve a query "produtos", retornando toda a lista
    def resolve_produtos(root, info):
        return produtos

# Define uma mutation (ação que altera dados) para adicionar um novo produto
class AdicionarProduto(graphene.Mutation):
    # Define os argumentos obrigatórios para adicionar um produto
    class Arguments:
        nome = graphene.String(required=True)
        preco = graphene.Float(required=True)

    # Define o retorno da mutation: o produto que foi adicionado
    produto = graphene.Field(Produto)

    # Função que realiza a adição do produto
    def mutate(root, info, nome, preco):
        novo = {"id": len(produtos) + 1, "nome": nome, "preco": preco}  # Cria um novo produto com ID automático
        produtos.append(novo)  # Adiciona o novo produto à lista
        return AdicionarProduto(produto=novo)  # Retorna o produto recém-adicionado

# Junta todas as mutations em uma classe principal
class Mutation(graphene.ObjectType):
    adicionar_produto = AdicionarProduto.Field()

# Cria o schema GraphQL com as queries e mutations definidas
schema = graphene.Schema(query=Query, mutation=Mutation)

# Cria o app Flask (servidor web leve em Python)
app = Flask(__name__)

# Define a rota "/graphql", que aceita requisições POST para usar a API GraphQL
@app.route("/graphql", methods=["POST"])
def graphql_api():
    data = request.get_json()  # Lê os dados JSON enviados na requisição
    result = schema.execute(data["query"], variables=data.get("variables"))  # Executa a query/mutation
    return jsonify(result.data)  # Retorna o resultado em formato JSON

# Rota padrão que apenas informa como usar a API
@app.route("/")
def home():
    return "API GraphQL disponível em /graphql (POST)"

# Inicia o servidor Flask em modo debug, se o script for executado diretamente
if __name__ == "__main__":
    app.run(debug=True)
