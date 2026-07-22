from app.extenstions import db

class Menu(db.Model):

    __tablename__ = "menu"
    id = db.Column(db.Integer, primary_key = True)
    dish_name = db.Column(db.String(100), nullable = False)
    preperation_time = db.Column(db.Integer, nullable = False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"), nullable = False)
