from config import db
from sqlalchemy.sql import func # type: ignore
from Models.users import User
from Models.staff import Staff

class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key = True)
    menu_name = db.Column(db.String(100), nullable = False)
    price = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String(100), nullable = False)
    created_at = db.Column(db.DateTime(timezone = True), default = func.now())
    client_id = db.Column(db.Integer, db.ForeignKey(User.user_id))
    staff_id = db.Column(db.Integer, db.ForeignKey(Staff.staff_id))