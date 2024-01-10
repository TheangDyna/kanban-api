from flask_restx import reqparse

register_parser = reqparse.RequestParser()
register_parser.add_argument('username', type=str, required=True, help='Username')
register_parser.add_argument('email', type=str, required=True, help='Email')
register_parser.add_argument('password', type=str, required=True, help='Password')