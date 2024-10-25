from flask import Flask
from flask_restful import Api
from resources.movie import Movie

app = Flask(__name__)
api = Api(app)

# Rutas
api.add_resource(Movie, '/movie', '/movie/<string:movie_id>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Permite el acceso desde Docker
