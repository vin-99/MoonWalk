from datetime import datetime
from app.models.restaurant import Restaurant
from app.models.order import Order
from app.services.kitchen_service import KitchenService


class KitchenProcessor:

    @staticmethod
    def process():

        restaurants = Restaurant.query.all()

        for restaurant in restaurants:

            cooking_orders = Order.query.filter_by(
                restaurant_id=restaurant.id,
                status="Cooking"
            ).all()

            for order in cooking_orders:

                elapsed = (
                    datetime.now() - order.started_at
                ).total_seconds()/60

                if elapsed >= order.estimated_time:

                    KitchenService.complete_order(order.id)
