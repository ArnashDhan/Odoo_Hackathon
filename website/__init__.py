from flask import Flask
from flask_sqlalchemy import SQLAlchemy
<<<<<<< HEAD
=======

db =SQLAlchemy()
DB_NAME ="database.db"
>>>>>>> upstream/ADW

db=SQLAlchemy
DB_NAME="database.db"
def create_app():
    app = Flask(__name__)
    app.config['secret_key'] = 'odoo_combat'
<<<<<<< HEAD
    app.config['SQLALHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'
=======
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://DB_NAME.sqlite3'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False

    db.init_app(app)

>>>>>>> upstream/ADW
    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/') 
    app.register_blueprint(auth,url_prefix='/') 
    return app