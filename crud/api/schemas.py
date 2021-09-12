from marshmallow import Schema, fields

class HeroiSchema(Schema):
    heroi_id = fields.Integer(description="Id do Heroi", required=True)
    nome = fields.String(description="Nome do Heroi", required=True)
    idade = fields.Integer(description="Idade do Heroi", required=True)
    criador = fields.String(description="Criador do Heroi", required=True)
