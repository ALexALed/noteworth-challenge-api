
from flask import Blueprint

root_blueprint = Blueprint('root', __name__)


@root_blueprint.route('/health/')
def health():
    return {'message': 'Healthy'}  # This will return as JSON by default with a 200 status code
