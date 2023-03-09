	
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


# inicializa app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
                                         basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# inicializa database
db = SQLAlchemy(app)
# inicializa marshmallow
marshmallow = Marshmallow(app)


# class/model pedido
class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mesa = db.Column(db.String(3))
    pedido = db.Column(db.String(200))
    quantidade = db.Column(db.Integer)
    valor = db.Column(db.Float)
    atendente = db.Column(db.String(100))

    def __init__(self, mesa, pedido, quantidade, valor, atendente):
        self.mesa = mesa
        self.pedido = pedido
        self.quantidade = quantidade
        self.valor = valor
        self.atendente = atendente


# schema pedido
class PedidoSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'mesa', 'pedido', 'quantidade', 'valor', 'atendente')


# inicializa schema pedido
pedido_schema = PedidoSchema()
pedidos_schema = PedidoSchema(many=True)

# gera/inclui um pedido
@app.route('/pedido', methods=['POST'])
def inclui_pedido():
    mesa = request.json['mesa']
    pedido = request.json['pedido']
    quantidade = request.json['quantidade']
    valor = request.json['valor']
    atendente = request.json['atendente']

    novo_pedido = Pedido(mesa, pedido, quantidade, valor, atendente)
    db.session.add(novo_pedido)
    db.session.commit()
    return pedido_schema.jsonify(novo_pedido)


# atualiza/corrige pedido
@app.route('/pedido/<id>', methods=['PUT'])
def atualiza_pedido(id):
    pedido = Pedido.query.get(id)

    mesa_atualizada = request.json['mesa']
    pedido_atualizado = request.json['pedido']
    quantidade_atualizada = request.json['quantidade']
    valor_atualizado = request.json['valor']
    atendente_atualizado = request.json['atendente']

    pedido.mesa = mesa_atualizada
    pedido.pedido = pedido_atualizado
    pedido.quantidade = quantidade_atualizada
    pedido.valor = valor_atualizado
    pedido.atendente = atendente_atualizado

    db.session.commit()
    return pedido_schema.jsonify(pedido)

# obtém a relação de todos os pedidos
@app.route('/pedidos', methods=['GET'])
def obtem_pedidos():
    relacao_de_pedidos = Pedido.query.all()
    resultado = pedidos_schema.dump(relacao_de_pedidos)
    return jsonify(resultado)

# obtém os dados de um pedido específico
@app.route('/pedido/<id>', methods=['GET'])
def obtem_pedido(id):
    dados_do_pedido = Pedido.query.get(id)
    resultado = pedido_schema.jsonify(dados_do_pedido)
    return resultado

# deleta um pedido
@app.route('/pedido/<id>', methods=['DELETE'])
def exclui_pedido(id):
    pedido_a_excluir = Pedido.query.get(id)
    db.session.delete(pedido_a_excluir)
    db.session.commit()
    resultado = pedido_schema.jsonify(pedido_a_excluir)
    return resultado


# inicializa app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
