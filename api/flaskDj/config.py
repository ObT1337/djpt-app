import os


class Config:
    SECRET_KEY = "dev"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        os.getcwd(), "instance", "flaskDj.sqlite"
    )
