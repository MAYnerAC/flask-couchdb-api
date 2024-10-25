import os

COUCHDB_URL = os.getenv('COUCHDB_URL', 'http://admin:admin@localhost:5984/')
DATABASE_NAME = 'movies'
