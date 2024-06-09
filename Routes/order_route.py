from flask import Blueprint # type:ignore

from Controllers.order_controller import index, add_order, view_order, newOrder, delete_order, update_Order

order = Blueprint('order' , __name__)

order.route('/order' , methods=['GET'] , strict_slashes=False)(index)
order.route('/add_order' , methods=['GET'] , strict_slashes=False)(add_order)
order.route('/create_order' , methods=['POST'] , strict_slashes=False)(newOrder)
order.route('/view/<order_id>' , methods=['GET'] , strict_slashes=False)(view_order)
order.route('/update/<order_id>' , methods=['GET' , "POST"] , strict_slashes=False)(update_Order)
order.route('/delete/<order_id>' , methods=['POST' , "DELETE"] , strict_slashes=False)(delete_order)
