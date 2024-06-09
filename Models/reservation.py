from config import db
from sqlalchemy.sql import func # type: ignore
from Models.client import Client

class Reservation(db.Model):
    reservation_id = db.Column(db.Integer, primary_key = True)
    table_name = db.Column(db.String(100), nullable = False)
    price = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String(100), nullable = False)
    created_at = db.Column(db.DateTime(timezone = True), default = func.now())
    client_id = db.Column(db.Integer, db.ForeignKey(Client.client_id))