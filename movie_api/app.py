from flask import Flask
from flask_restx import Api
from resources.movie import movie_ns  # Añadir esta línea para importar el namespace

app = Flask(__name__)
api = Api(app, version='1.0', title='Movie API', description='A simple Movie API')

# Rutas
api.add_namespace(movie_ns, path='/movie')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Permite el acceso desde Docker
