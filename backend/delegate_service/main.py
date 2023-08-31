from flask import Flask, Blueprint
from flask_cors import CORS
from dotenv import load_dotenv

from app.controllers.delegate import controller as delegate_controller

if __name__ == "__main__":
    if load_dotenv() is False:
        raise(Exception(".env file not found"))

    webservice = Flask("delegate_service")

    blueprint = Blueprint('2023', __name__, url_prefix='/delegate-service')
    blueprint.register_blueprint(delegate_controller)
    CORS(blueprint, resources=r'/delegate-service/*')

    webservice.register_blueprint(blueprint)
    webservice.run(host="0.0.0.0")
