from flask import Blueprint # type: ignore
from Controllers.client_controller import index, add_user, newUser

client = Blueprint('client', __name__)

client.route("/", methods=['GET'], strict_slashes=False)(index)
client.route("/add_client", methods=['GET'], strict_slashes=False)(add_user)
client.route('/new_client', methods=["POST"], strict_slashes=False)(newUser)
# client.route('/delet/<id>', methods=["DELETE", "POST"], strict_slashes=False)(delete_user)
# client.route('/updat/<id>', methods=["POST", "GET"], strict_slashes=False)(update_user)