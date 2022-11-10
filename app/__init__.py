from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
# os: operating system


db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(testing=None):
    # __name__ stores the name of the module we're in
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    if testing is None:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")
    # psycopg2 is a python library
    # The last part /bikes_development will be change what your database name it is 
    

    from app.models.bike import Bike

    db.init_app(app)
    migrate.init_app(app, db)
    # (method) init_app

    from .routes.bike import bike_bp
    app.register_blueprint(bike_bp)

    from .routes.cyclist import cyclist_bp
    app.register_blueprint(cyclist_bp)

    return app