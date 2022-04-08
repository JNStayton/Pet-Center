"""Models for Pet Center"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database; call this function in app.py"""
    db.app = app
    db.init_app(app)

# models here

class Pet(db.Model):
    """A model for Pets"""
    __tablename__="pets"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    name = db.Column(db.String, nullable = False)

    species = db.Column(db.String, nullable = False)

    photo_url = db.Column(db.String(2048), nullable = False)

    age = db.Column(db.Integer)

    notes = db.Column(db.String)

    available = db.Column(db.Boolean, default = True)