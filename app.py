from crud import app
from os import environ
# objeto de mapeamento que representa as variaveis ambientais do usuario

if __name__ == '__main__':
    SERVER_HOST = environ.get('SERVER_HOST', 'localhost')
    app.run(host=SERVER_HOST, port=8080, debug=(not environ.get('ENV') == 'PRODUCTION'), threaded=True)
    # threaded = True aceita requisições simultâneas