from flask import Flask # type: ignore
from flask_migrate import Migrate # type: ignore
from config import db

# from routes.article_route import article
from Routes.wep_route import web
from Routes.menu_route import menu
from Routes.order_route import order
from Routes.reservation_route import reservation
from Routes.staff_route import staff
from Routes.users_route import auth

app = Flask(__name__)

app.config.from_object('config')
db.init_app(app)
migrate = Migrate(app, db)

# app.register_blueprint(article, url_prefix='/')
app.register_blueprint(web, url_prefix='/')
app.register_blueprint(menu, url_prefix='/menu')
app.register_blueprint(order, url_prefix='/order')
app.register_blueprint(reservation, url_prefix='/reservation')
app.register_blueprint(staff, url_prefix='/staff')
app.register_blueprint(auth, url_prefix='/auth')


if __name__ == "__main__":
    app.run(debug=True, port=3000)  