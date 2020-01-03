from flask import Blueprint, Flask
from flask_restful import Api, Resource
from models import db
from routes.post import post_blueprint
import config

app = Flask(__name__)

# Config
app.config.from_object("config")
app.secret_key = config.SECRET_KEY

# Blueprint
app.register_blueprint(post_blueprint)

# Database
db.init_app(app)

if __name__ == "__main__":
    app.run(debug=config.DEBUG, host="0.0.0.0", port=config.PORT)
