from flask_restful import Resource, reqparse
from db import get_db
from models.movie_model import create_movie_data

# Configurar los argumentos necesarios para la API
parser = reqparse.RequestParser()
parser.add_argument('title', type=str, required=True, help="Title cannot be blank.")
parser.add_argument('year', type=int, required=True, help="Year cannot be blank.")
parser.add_argument('genre', type=str, required=True, help="Genre cannot be blank.")
parser.add_argument('director', type=str, required=True, help="Director cannot be blank.")
parser.add_argument('rating', type=float, required=True, help="Rating cannot be blank.")
parser.add_argument('duration', type=int, required=True, help="Duration cannot be blank.")

class Movie(Resource):
    def get(self, movie_id=None):
        db = get_db()
        if movie_id:
            movie = db.get(movie_id)
            if movie and movie.get("status") == "active":
                return movie, 200
            return {'error': 'Not found or inactive'}, 404
        else:
            movies = [doc for doc in db if db[doc].get("status") == "active"]
            return movies, 200

    def post(self):
        args = parser.parse_args()
        db = get_db()
        movie_data = create_movie_data(
            title=args['title'],
            year=args['year'],
            genre=args['genre'],
            director=args['director'],
            rating=args['rating'],
            duration=args['duration']
        )
        movie_id, movie_rev = db.save(movie_data)
        return {'id': movie_id, 'rev': movie_rev}, 201

    def put(self, movie_id):
        args = parser.parse_args()
        db = get_db()
        movie = db.get(movie_id)
        if not movie:
            return {'error': 'Not found'}, 404

        movie.update(create_movie_data(
            title=args['title'],
            year=args['year'],
            genre=args['genre'],
            director=args['director'],
            rating=args['rating'],
            duration=args['duration']
        ))
        db.save(movie)
        return movie, 200

    def delete(self, movie_id):
        db = get_db()
        movie = db.get(movie_id)
        if not movie:
            return {'error': 'Not found'}, 404

        movie["status"] = "inactive"
        db.save(movie)
        return {'message': 'Movie marked as inactive'}, 200
