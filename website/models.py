from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.column("id", db.Integer, primary_key=True)
    name = db.column(db.String(100))
    email = db.column(db.String(100))