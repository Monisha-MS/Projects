from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"
app = Flask(__name__)
ma=Marshmallow()

def create_app():
    app.config['SECRET_KEY'] = 'It\'s a secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    from .views import views
    app.register_blueprint(views, url_prefix = '/')
    
    
    from .models import Product
    
    with app.app_context():
        db.create_all()
    return app



def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')