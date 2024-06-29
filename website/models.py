from . import db
from flask_login import UserMixin

class user(db.model,UserMixin):
    id=db.Column(db.Integer, primary_key =True)
    email= db.Column(db.String(150),unique=True)
    Password=db.Column(db.string(150))
    first_name=db.Column(db.String(150))
    
