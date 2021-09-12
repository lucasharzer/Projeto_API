from flask import Flask, Blueprint
from flask_restplus import Api
from werkzeug.contrib.fixers import ProxyFix
from crud.api.view import api as heroi_ns

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
# Proxyfix facilita ingestão de certificado SSL
blueprint = Blueprint('api', __name__)
app.register_blueprint(blueprint)

api = Api(app, title='Projeto API de Herois', version='1.0', description='API Python Flask com Swagger', prefix='/api')
api.add_namespace(heroi_ns, path='/heroi')
