from flask import Flask
from flask_assets import Bundle, Environment
from app.views.index import index
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    assets = Environment(app)

    css = Bundle("src/main.css", output="dist/main.css")

    assets.register("css", css)
    css.build()

    app.register_blueprint(index)

    return app