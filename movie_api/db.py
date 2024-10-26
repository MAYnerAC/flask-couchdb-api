import couchdb
from config import COUCHDB_URL, DATABASE_NAME

def get_db():
    couch = couchdb.Server(COUCHDB_URL)
    if DATABASE_NAME in couch:
        return couch[DATABASE_NAME]
    else:
        return couch.create(DATABASE_NAME)  # Crea la bd si no existe
