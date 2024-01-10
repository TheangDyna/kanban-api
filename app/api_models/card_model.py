from flask_restx import fields
from ..extensions import api

card_model = api.model('Column', {
    'id': fields.Integer,
    'column_id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'user_id': fields.Integer,
    'deadline': fields.DateTime,
    'created_at': fields.DateTime,
    'updated_at': fields.DateTime,
})