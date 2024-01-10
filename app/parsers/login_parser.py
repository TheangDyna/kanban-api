from flask_restx import reqparse

login_parser = reqparse.RequestParser()
login_parser.add_argument('email', type=str, required=True, help='Email')
login_parser.add_argument('password', type=str, required=True, help='Password')