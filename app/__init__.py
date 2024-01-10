from flask import Flask

from .extensions import api, db
from .config import config
from .resources.user_resource import ns as user_resource
from .resources.board_resource import ns as board_resource
from .resources.column_resource import ns as column_resource
from .resources.card_resource import ns as card_resource

app = Flask(__name__)

app.config.from_object(config)

api.init_app(app)

api.add_namespace(user_resource)
api.add_namespace(board_resource)
api.add_namespace(column_resource)
api.add_namespace(card_resource)

with app.app_context():
    db.init_app(app)
    db.create_all()