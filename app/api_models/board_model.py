from flask_restx import fields
from ..extensions import api

board_model = api.model('Board', {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'created_at': fields.DateTime,
    'updated_at': fields.DateTime,
})