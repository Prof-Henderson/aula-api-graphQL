from flask import Flask, request, jsonify
import graphene

# Modelo
class Produto(graphene.ObjectType):
    id = graphene.Int()
    nome = graphene.String()
    preco = graphene.Float()

# Lista simulando banco
produtos = [
    {"id": 1, "nome": "Camiseta", "preco": 50.00},
    {"id": 2, "nome": "Tênis", "preco": 120.00}
]

# Query
class Query(graphene.ObjectType):
    produto = graphene.Field(Produto, id=graphene.Int())
    produtos = graphene.List(Produto)

    def resolve_produto(root, info, id):
        return next((p for p in produtos if p['id'] == id), None)

    def resolve_produtos(root, info):
        return produtos

# Mutation
class AdicionarProduto(graphene.Mutation):
    class Arguments:
        nome = graphene.String(required=True)
        preco = graphene.Float(required=True)

    produto = graphene.Field(Produto)

    def mutate(root, info, nome, preco):
        novo = {"id": len(produtos) + 1, "nome": nome, "preco": preco}
        produtos.append(novo)
        return AdicionarProduto(produto=novo)

class Mutation(graphene.ObjectType):
    adicionar_produto = AdicionarProduto.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

# Flask App
app = Flask(__name__)

@app.route("/graphql", methods=["POST"])
def graphql_api():
    data = request.get_json()
    result = schema.execute(data["query"], variables=data.get("variables"))
    return jsonify(result.data)

@app.route("/")
def home():
    return "API GraphQL disponível em /graphql (POST)"

if __name__ == "__main__":
    app.run(debug=True)
