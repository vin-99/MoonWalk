class Config:
    DEBUG = True

    RESTAURANT_NAME = "MoonWalk"

    SQLALCHEMY_DATABASE_URI = "sqlite:///moonwalk.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    KITCHEN_CAPACITY = 5

    DEFAULT_PREPARATION_TIME = 15