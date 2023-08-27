from flask import Flask, Blueprint
from flask_cors import CORS
from dotenv import load_dotenv

from app.controller.rfb import controller as rfb_controller

if __name__ == "__main__":
    if load_dotenv() is False:
        raise(Exception(".env file not found"))

    webservice = Flask("OPEI 2023 RFB service")

    blueprint = Blueprint('2023', __name__, url_prefix='/v2023')
    blueprint.register_blueprint(rfb_controller)
    CORS(blueprint, resources=r'/v2023/*')

    webservice.register_blueprint(blueprint)
    webservice.run(host="0.0.0.0")
