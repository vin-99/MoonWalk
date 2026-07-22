from datetime import datetime
from app.models.chef import Chef
from app.models.order import Order
from app.extenstions import db

class KitchenService():

    @staticmethod
    def get_available_chef(restaurant_id):
        chef = Chef.query.filter_by(restaurant_id=restaurant_id, is_available = True).first()
        return chef
    
    @staticmethod
    def get_next_waiting_order(restaurant_id):
        order = Order.query.filter_by(restaurant_id = restaurant_id, status = "Waiting").first()
        return order

    @staticmethod
    def assign_waiting_order(restaurant_id):
        chef = KitchenService.get_available_chef(restaurant_id)
        waiting_order = KitchenService.get_next_waiting_order(restaurant_id)
        if chef and waiting_order:
            waiting_order.chef_name = chef.name
            waiting_order.status = "Cooking"
            waiting_order.started_at = datetime.now()
            chef.is_available = False

            db.session.commit()

    @staticmethod
    def complete_order(id):
        order = Order.query.get(id)
        if order is None:
            return None
        if order.status != "Cooking":
            return None
        order.status = "Completed"

        chef = Chef.query.filter_by(restaurant_id=order.restaurant_id, name = order.chef_name).first()
        if chef:
            chef.is_available = True
        db.session.commit()
        KitchenService.assign_waiting_order(order.restaurant_id)
        return order
    
    @staticmethod
    def calculate_waiting_time(restaurant_id):
        busy_chef = Chef.query.filter_by(restaurant_id=restaurant_id, is_available = False).all()
        remaining_time = []
        for chef in busy_chef:
            order = Order.query.filter_by(restaurant_id=restaurant_id, chef_name = chef.name, status="Cooking").first()
            if order:
                elapsed = (datetime.now() - order.started_at).total_seconds()/60
                remaining = max(0, (order.estimated_time - elapsed))
                remaining_time.append(remaining)
        if remaining_time:
            return min(remaining_time)
        return 0

