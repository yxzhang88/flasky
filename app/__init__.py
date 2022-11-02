from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # __name__ stores the name of the module we're in
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/bikes_development'
    # psycopg2 is a python library
    # The last part /bikes_development will be change what your database name it is (edited) 
    
    from app.models.bike import Bike

    db.init_app(app)
    migrate.init_app(app, db)
    # (method) init_app

    from app.routes.bike import bike_bp
    app.register_blueprint(bike_bp)

    return app