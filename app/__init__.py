from flask import Flask
from app.routes.home_routes import home_bp
from app.routes.order_routes import order_bp
from app.config import Config
from app.extenstions import db
from app.models.order import Order
from app.models.chef import Chef
from app.models.menu import Menu
from app.models.restaurant import Restaurant
from app.seed import seed_data
from app.schedular import start_schedular

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    db.init_app(app)

    app.register_blueprint(home_bp)
    app.register_blueprint(order_bp)

    #Create Database
    with app.app_context():
        db.create_all()
        #seed_data()
        start_schedular(app)

    return app
