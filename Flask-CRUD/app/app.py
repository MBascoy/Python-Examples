
from app.routes import include_routers
from flask import Flask
from app.models.task import db

def start_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud_example.db'
    db.init_app(app)

    include_routers(app)
    
    with app.app_context():
        db.create_all()

    return app
