# A standard pytest file that holds 
# test configurations and common test helper functions
# https://learn-2.galvanize.com/cohorts/3432/blocks/1310/content_files/api-6-testing/test-setup.md


import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.bike import Bike


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()
    
    with app.app_context():
        db.create_all()
        yield app
    
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def two_bikes(app):
    bike1 = Bike(name="June", price=90, size=16, type="auto")
    bike2 = Bike(name="Setp", price=190, size=20, type="motor")

    db.session.add(bike1)
    db.session.add(bike2)
    db.session.commit()
