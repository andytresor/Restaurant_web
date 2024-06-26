from flask import Blueprint # type:ignore

from Controllers.staff_controller import index, add_staff, view_staff, newStaff, delete_staff, update_staff
staff = Blueprint('staff' , __name__)

staff.route('/staff' , methods=['GET'] , strict_slashes=False)(index)
staff.route('/add_staff' , methods=['GET'] , strict_slashes=False)(add_staff)
staff.route('/create_staff' , methods=['POST'] , strict_slashes=False)(newStaff)
staff.route('/view/<staff_id>' , methods=['GET'] , strict_slashes=False)(view_staff)
staff.route('/update/<staff_id>' , methods=['GET' , "POST"] , strict_slashes=False)(update_staff)
staff.route('/delete/<staff_id>' , methods=['POST' , "DELETE"] , strict_slashes=False)(delete_staff)
# staff.route('/user_id' , methods=['GET'] , strict_slashes=False)(user_id)
