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
    
    # FK = foreignKey 'cyclist.id' here the cyclist is the attribute
    cyclist_id = db.Column(db.Integer, db.ForeignKey('cyclist.id'))
    cyclist = db.relationship("Cyclist", back_populates="bikes")
    # "bikes" is the entity in another database
    # "Cyclist" here is the class name

    def to_dict(self):
        return {
            "id":self.id,
            "name": self.name,
            "price": self.price,
            "size": self.size,
            "type": self.type
        }
    
    @classmethod
    def from_dict(cls, data_dict):
        #cls represents the whole class variables
        if "name" in data_dict and "price" in data_dict and\
            "size" in data_dict and "type" in data_dict:
            new_obj = cls(name=data_dict["name"],price=data_dict["price"],
                          size=data_dict["size"],type=data_dict["type"])
            return new_obj
        