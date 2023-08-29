from flask import Flask, Blueprint
from flask_cors import CORS
from dotenv import load_dotenv

from app.controller.cpf import controller as cpf_controller

if __name__ == "__main__":
    if load_dotenv() is False:
        raise(Exception(".env file not found"))

    webservice = Flask("CPF_service")

    blueprint = Blueprint('2023', __name__, url_prefix='/rfb-cpf')
    blueprint.register_blueprint(cpf_controller)
    CORS(blueprint, resources=r'/rfb-cpf/*')

    webservice.register_blueprint(blueprint)
    webservice.run(host="0.0.0.0")
