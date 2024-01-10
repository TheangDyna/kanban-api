from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_restx import Namespace


api = Api()
db = SQLAlchemy()
ns = Namespace('api')