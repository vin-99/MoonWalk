from app.extenstions import db

class Restaurant(db.Model):

    __tablename__ = "restaurants"

    id = db.Column(db.Integer, nullable = False, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    location = db.Column(db.String(100), nullable = False)

    chefs = db.relationship("Chef", backref = "restaurant", lazy = True)
    menu_items = db.relationship("Menu", backref = "restaurant", lazy = True)
    orders = db.relationship("Order", backref = "restaurant", lazy = True)
