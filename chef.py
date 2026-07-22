from app.extenstions import db

class Chef(db.Model):

    __tablename__ = "chefs"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    is_available = db.Column(db.Boolean, default = True, nullable = False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"), nullable = False)