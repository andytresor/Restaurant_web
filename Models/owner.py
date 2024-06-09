from config import db
from sqlalchemy.sql import func # type: ignore

class Owner(db.Model):
    owner_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
