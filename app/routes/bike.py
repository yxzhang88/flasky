from flask import Blueprint, jsonify, request, abort, make_response
from app import db
from app.models.bike import Bike

# class Bike:
#     def __init__(self, id, name, price, size, type):
#         self.id = id
#         self.name = name
#         self.price = price
#         self.size = size
#         self.type = type

# hardcode
# bikes = [
#     Bike(5, "Nina", 100, 48, "gravel"),
#     Bike(8, "Bike 3000", 1000, 50, "hybrid"),
#     Bike(2, "Auberon", 2000, 52, "electonic")
# ]

# b/c we created a new table, so we dont need the above code anymore
# instead, we add the below to the top on the file
# from app import db
# from app.models.bike import Bike


bike_bp = Blueprint("bike_bp", __name__, url_prefix="/bike")

# helper function
def get_one_bike_or_abort(bike_id):
    try:
        bike_id = int(bike_id)
    except ValueError:
        response_str = f"Invalid Bike ID: '{bike_id}' must be an integer"
        abort(make_response(jsonify({"message":response_str}), 400))
        
    matching_bike = Bike.query.get(bike_id)

    if not matching_bike:
        response_str = f"Bike ID: '{bike_id}' was not found in the database"
        abort(make_response(jsonify({"message":response_str}), 404))
    
    return matching_bike


@bike_bp.route("", methods=["POST"])
def add_bike():
    request_body = request.get_json()

    new_bike = Bike(
        name = request_body["name"],   
        price = request_body["price"],
        size = request_body["size"],
        type = request_body["type"]
    )

    db.session.add(new_bike)
    db.session.commit()

    return {"id": new_bike.id, "name": new_bike.name, "price": new_bike.price}, 201
    

@bike_bp.route("", methods=["GET"])
def get_all_bikes():
    # query 
    name_param = request.args.get("name")

    if name_param is None:
        bikes = Bike.query.all()
    else:
        bikes = Bike.query.filter_by(name=name_param)

    response = []
    for bike in bikes:
        bike_dict = {
            "id": bike.id,
            "name": bike.name,
            "price": bike.price,
            "size": bike.size,
            "type": bike.type
        }
        response.append(bike_dict)
    return jsonify(response), 200
    


@bike_bp.route("/<bike_id>", methods = ["GET"])
def get_one_bike(bike_id):
    #  # see if bike_id can be converted to be an integer
    # try:
    #     bike_id = int(bike_id)
    # except ValueError:
    #     response_str = f"Invalid Bike ID: '{bike_id}' must be an integer"
    #     return jsonify({"message": response_str}), 400
    # # try-except: try to convert to an int if error occurs, catch it and raise the error
    # # after the try-except: bike_id will be a valid int

    # looping through data to find a bike with matching bike_id
    # if found: return that bike's data with 200 response code
    # for bike in bikes:
    #     if bike.id == bike_id:
    #         bike_dict = {
    #             "id": bike.id,
    #             "name": bike.name,
    #             "price": bike.price,
    #             "size": bike.size,
    #             "type": bike.type
    #         }
    #         return jsonify(bike_dict), 200
        
    # after the loop: the bike with matching bike_id not found,
    # we will 404 response code
    # response_message = f"Could not find the bike id {bike_id}"
    # return jsonify({"message": response_message}), 404


    chosen_bike = get_one_bike_or_abort(bike_id)
    bike_dict = {
        "id": chosen_bike.id,
        "name": chosen_bike.name,
        "price": chosen_bike.price,
        "size": chosen_bike.size,
        "type": chosen_bike.type
    }
    return jsonify(bike_dict), 200


@bike_bp.route("/<bike_id>", methods=["PUT"])
def update_bike_with_new_val(bike_id):
    chosen_bike = get_one_bike_or_abort(bike_id)
    request_body = request.get_json()

    if "name" not in request_body or \
       "size" not in request_body or \
       "price" not in request_body or \
       "type" not in request_body:
        return jsonify({"message": "Request must include name, size, price, and type"})

    chosen_bike.name = request_body["name"]
    chosen_bike.name = request_body["size"]
    chosen_bike.name = request_body["price"]
    chosen_bike.name = request_body["type"]

    db.session.commit()

    return jsonify({"message": f"Successfully replaced bike with id {bike_id}"}, 200)


@bike_bp.route("/<bike_id>", methods=["DELETE"])
def delete_one_bike(bike_id):
    chosen_bike = get_one_bike_or_abort(bike_id)
    db.session.delete(chosen_bike)
    db.session.commit()
    return jsonify({"message": f"Successfully deleted bike with id {bike_id}"}, 200)


