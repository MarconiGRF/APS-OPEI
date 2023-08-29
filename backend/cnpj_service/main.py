from flask import Flask, Blueprint
from flask_cors import CORS
from dotenv import load_dotenv

from app.controller.cnpj import controller as cnpj_controller

if __name__ == "__main__":
    if load_dotenv() is False:
        raise(Exception(".env file not found"))

    webservice = Flask("CNPJ_service")

    blueprint = Blueprint('2023', __name__, url_prefix='/rfb-cnpj')
    blueprint.register_blueprint(cnpj_controller)
    CORS(blueprint, resources=r'/rfb-cnpj/*')

    webservice.register_blueprint(blueprint)
    webservice.run(host="0.0.0.0")
