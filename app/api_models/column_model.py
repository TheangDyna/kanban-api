from flask_restx import fields
from ..extensions import api

column_model = api.model('Column', {
    'id': fields.Integer,
    'board_id': fields.Integer,
    'name': fields.String,
    'created_at': fields.DateTime,
    'updated_at': fields.DateTime,
})