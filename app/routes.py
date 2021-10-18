from flask import Blueprint

hello_world_bp = Blueprint("hello_world", __name__)
dog_bp = Blueprint("dog", __name__)


class Dog:
    def __init__(self, id, name, breed, tricks=None):
        self.id = id
        self.name = name
        self.breed = breed
        if not tricks:
            tricks = []
        self.tricks = tricks

dogs = [
    Dog(1, "mac", "greyhound"),
    Dog(2, "sparky", "schnauzer"),
    Dog(3, "teddy", "golden retriever")
]



@hello_world_bp.route("/hello-world", methods=["GET"])
def hello_world():
    return "hello world!"

@