from flask import Blueprint
from backend.app.controllers.delegate import controller as delegate_controller
from backend.app.controllers.insitution import controller as institution_controller
from backend.app.controllers.relation import controller as relation_controller
from backend.app.controllers.student import controller as student_controller
from backend.app.controllers.certificate import controller as certificate_controller

facade = Blueprint('facade', __name__, url_prefix='/v2023')
facade.register_blueprint(delegate_controller)
facade.register_blueprint(institution_controller)
facade.register_blueprint(student_controller)
facade.register_blueprint(relation_controller)
facade.register_blueprint(certificate_controller)