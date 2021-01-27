import sqlite3
from flask import g

DATABASE = 'url_shortener.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = sqlite3.connect(DATABASE)
        db = g._database
    return db
