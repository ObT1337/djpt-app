from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flaskDj import config, factory

db = SQLAlchemy()
app = Flask(
    __name__,
    static_folder="../build",
    static_url_path="/",
    instance_relative_config=True,
)
migrate = Migrate(app, db)
app.db = db
app.migrate = Migrate

if __name__ == "flaskDj":
    app = factory.create_app(app, config_object=config.DevelopmentConfig)
