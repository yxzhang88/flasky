from flask import Flask

def create_app():
    # __name__ store the name of the module we're in
    app = Flask(__name__)

    from .routes.dog_routes import dog_bp
    app.register_blueprint(dog_bp)

    from .routes.cat_routes import cat_bp
    app.register_blueprint(cat_bp)

    return app