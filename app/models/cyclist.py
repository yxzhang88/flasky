# from app import db

# class Cyclist(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.name(db.String)
#     bikes = db.relationship("Bike", back_populates="cyclist")
#     # bikes from where
#     # what is line 6 means

#     def to_dict(self):
#         bikes_list = [bike.to_dict() for bike in self.bikes]
#         # self.bikes is from line 6

#         cyclist_dict =  {
#             "id":self.id,
#             "name": self.name,  
#             "bikes":bikes_list
#         }
#         return cyclist_dict

#     @classmethod
#     def from_dict(cls, data_dict):
#         #cls represents the whole class variables
#         if "name" in data_dict:
#             new_obj = cls(name=data_dict["name"])
#             return new_obj


from app import db

class Cyclist(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    bikes = db.relationship("Bike", back_populates="cyclist")
    # bieks here is related to the back_pupoltates 
    # cyclist is related to the cyclist = db.relationship("Cyclist",back_populates="bikes")

    def to_dict(self):
        bikes_list = [bike.to_dict() for bike in self.bikes]
        cyclist_dict = {
            "id": self.id,
            "name": self.name,
            "bikes": bikes_list
        }
        return cyclist_dict

    @classmethod
    def from_dict(cls, data_dict):
        #check data_dict has all valid attributes
        #helps prevent KeyError
        if "name" in data_dict:
            new_obj = cls(name=data_dict["name"])
            
            return new_obj
        #if not, can look into raising an error with make_response and abort(); did not have