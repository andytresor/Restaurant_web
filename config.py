from flask_sqlalchemy import SQLAlchemy # type: ignore

db = SQLAlchemy()

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:pamelajo25@127.0.0.1:3306/restaurant_web'
SQLALCHEMY_TRACK_MODIFICATIONS = False