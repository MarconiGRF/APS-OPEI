from flask import Blueprint

controller = Blueprint('student_controller', __name__, url_prefix='/student')


@controller.route('/')
def main():
    return "Howdy from student"
