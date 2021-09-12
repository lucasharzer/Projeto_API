from crud.api.schemas import HeroiSchema
from flask_restplus import Resource, Namespace, fields
from flask import request
from crud.api.registration import Heroi

api = Namespace('Heroi', description='Manutenção de dados de herois')
modelo = api.model('HeroiModel', {
    'heroi_id': fields.Integer,
    'nome': fields.String,
    'idade': fields.Integer,
    'criador': fields.String,
})

@api.route('/')
class HeroiView(Resource):
    @api.response(200, 'Busca realizada com sucesso!')
    def get(self):
        return Heroi.listar(), 200
    
    @api.expect(modelo)
    @api.expect(HeroiSchema(), validate=True)
    def post(self):
        return Heroi.cadastrar(request.json), 201

@api.route('/<heroi_id>')
class HeroiIdView(Resource):
    @api.response(200, 'Busca realizada com sucesso!')
    def get(self, heroi_id:int):
        return Heroi.listar(int(heroi_id)), 200

    @api.response(200, 'Busca realizada com sucesso!')
    @api.param('nome', 'Nome do Heroi')
    @api.param('idade', 'idade do Heroi')
    @api.param('criador', 'Criador do Heroi')
    def put(self, heroi_id:int):
        return Heroi.atualizar(int(heroi_id), request.json), 201

    def delete(self, heroi_id:int):
        return Heroi.deletar(int(heroi_id)), 200