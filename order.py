from app.extenstions import db

class Order(db.Model):

    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key = True)
    customer_name = db.Column(db.String(100), nullable = False)
    dish = db.Column(db.String(100), nullable = False)
    quantity = db.Column(db.Integer, nullable = False)
    status = db.Column(db.String(100), nullable = False)
    chef_name = db.Column(db.String(100), nullable = True)
    estimated_time = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, nullable = False)
    started_at = db.Column(db.DateTime, nullable=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"), nullable = False)