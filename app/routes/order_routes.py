from datetime import datetime
from flask import Blueprint, request, jsonify, current_app
from app.extenstions import db
from app.models.order import Order
from app.services.order_service import OrderService
from app.services.kitchen_service import KitchenService

order_bp = Blueprint("orders", __name__)

@order_bp.route("/orders", methods = ["GET"])
def get_orders():

    orders = Order.query.all()
    result = []

    for order in orders:
        result.append({
            "ID":order.id,
            "Customer_Name":order.customer_name,
            "Dish":order.dish,
            "Quantity":order.quantity,
            "Status":order.status,
            "Estimated_Time":order.estimated_time
        })

    return jsonify(result), 200

@order_bp.route("/orders/<int:id>", methods= ["GET"])
def get_order(id):

    order = db.session.get(Order, id)

    if order is None:
        return jsonify({"message":
        "Order Not Found"}), 404
    
    return jsonify({
        "Order_ID":order.id,
        "Customer_Name": order.customer_name,
        "Dish": order.dish,
        "Quantity": order.quantity,
        "Status": order.status,
        "Prepration_Time": order.estimated_time,
        "Created_At": order.created_at
    }), 200

@order_bp.route("/orders/<int:id>", methods=["PUT"])
def update_order(id):

    order = db.session.get(Order, id)

    if order is None:
        return jsonify({
            "message":"Order Not Found"
        }), 404
    
    data = request.get_json()
    order.status = data["status"]
    db.session.commit()

    return jsonify({
        "message":"Order Updated Successfully"
    }), 200

@order_bp.route("/orders", methods = ["POST"])
def create_order():

    data = request.get_json()
    print(data)

    OrderService.create_order(data)

    return jsonify({
        "message":"Order Created Successfully"
    }), 201

@order_bp.route("/orders/<int:id>", methods= ["DELETE"])
def delete_order(id):

    order = db.session.get(Order, id)

    if order is None:
        return jsonify({
            "message": "Order Not Found"
        }), 404
    
    db.session.delete(order)
    db.session.commit()

    return jsonify({
        "message": "Order Deleted Successfully"
    }), 200


# @order_bp.route("/orders/<int:id>/complete", methods=["PUT"])
# def complete_order(id):
#     order = KitchenService.complete_order(id)

#     if order is None:
#         return jsonify({"error": "Order not found or not cooking"}), 404

#     return jsonify({"message": "Order completed"})
