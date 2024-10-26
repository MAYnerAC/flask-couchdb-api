from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from resources.movie import movie_ns

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)  # Habilitar CORS *
api = Api(app, version='1.0', title='Movie API', description='A simple Movie API')

# Registrar el namespace
api.add_namespace(movie_ns, path='/movie')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Permite el acceso desde Docker
