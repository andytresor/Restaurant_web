from flask import Blueprint # type:ignore

from Controllers.reservation_controller import index, add_reservation, newReservation, delete_reservation, update_reservation

reservation = Blueprint('reservation' , __name__)

reservation.route('/reservation' , methods=['GET'] , strict_slashes=False)(index)
reservation.route('/add_reservation' , methods=['GET'] , strict_slashes=False)(add_reservation)
reservation.route('/create_reservation' , methods=['POST'] , strict_slashes=False)(newReservation)
reservation.route('/update/<reservation_id>' , methods=['GET' , "POST"] , strict_slashes=False)(update_reservation)
reservation.route('/delete/<reservation_id>' , methods=['POST' , "DELETE"] , strict_slashes=False)(delete_reservation)
