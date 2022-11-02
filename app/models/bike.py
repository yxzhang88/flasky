from app import db
# db is the SQLAlchemy


# Model: A SQLAlchemy declarative model class, 
# Subclass this to define database models
# db was declare in the app/__init__.py
class Bike(db.Model): # create a table here
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    size = db.Column(db.Integer)
    type = db.Column(db.String)
    # here, go back to app.__init__.py to add this: from app.models.bike import Bike

    