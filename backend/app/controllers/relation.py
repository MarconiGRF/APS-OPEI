from flask import Blueprint

controller = Blueprint('relation_controller', __name__, url_prefix='/relation')


@controller.route('/')
def main():
    return "Howdy from relation"
