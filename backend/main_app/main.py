from flask import Flask, Blueprint
from flask_cors import CORS
from dotenv import load_dotenv

from app.controllers.delegate import controller as delegate_controller
from app.controllers.institution import controller as institution_controller
from app.controllers.relation import controller as relation_controller
from app.controllers.student import controller as student_controller
from app.controllers.certificate import controller as certificate_controller

if __name__ == "__main__":
    if load_dotenv() is False:
        raise(Exception(".env file not found"))

    webservice = Flask("OPEI 2023 Webservice")

    blueprint = Blueprint('2023', __name__, url_prefix='/v2023')
    blueprint.register_blueprint(institution_controller)
    blueprint.register_blueprint(delegate_controller)
    blueprint.register_blueprint(relation_controller)
    blueprint.register_blueprint(student_controller)
    blueprint.register_blueprint(certificate_controller)
    CORS(blueprint, resources=r'/v2023/*')

    webservice.register_blueprint(blueprint)
    webservice.run(host="0.0.0.0")
