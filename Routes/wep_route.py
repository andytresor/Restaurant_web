from flask import Blueprint

from Controllers.web_controller import account, index

web = Blueprint('web', __name__)

web.route('/', strict_slashes=False)(index)
web.route('/account', strict_slashes=False)(account)