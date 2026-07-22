from datetime import datetime
from flask import current_app, jsonify

from app.extenstions import db
from app.models.order import Order
from app.models.menu import Menu

from app.services.kitchen_service import KitchenService

class OrderService:

    @staticmethod
    def create_order(data):
        menu_item = Menu.query.filter_by(restaurant_id=data["restaurant_id"], dish_name = data["dish"]).first()
        if menu_item is None:
            raise ValueError("Dish Not Found.")
        chef = KitchenService.get_available_chef(data["restaurant_id"])
        prepration_time = (menu_item.preperation_time) * data["quantity"]

        if chef:
            status = "Cooking"
            chef_name = chef.name
            started_at = datetime.now()
            chef.is_available = False
            estimated_time = prepration_time

        else:
            status = "Waiting"
            chef_name = "No-one"
            started_at = None
            waiting_time = KitchenService.calculate_waiting_time(data["restaurant_id"])
            estimated_time = prepration_time + waiting_time

        order = Order(
            customer_name = data["customer_name"],
            dish = data["dish"],
            quantity =  data["quantity"],
            status = status,
            chef_name = chef_name,
            estimated_time = estimated_time,
            created_at = datetime.now(),
            started_at = started_at,
            restaurant_id=data["restaurant_id"]
        )
        db.session.add(order)
        db.session.commit()

        return order