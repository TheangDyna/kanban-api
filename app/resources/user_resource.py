from flask_restx import Resource
from werkzeug.security import generate_password_hash, check_password_hash

from ..extensions import db, ns
from ..models import User
from ..api_models import user_model
from ..parsers import login_parser, register_parser

@ns.route('/register')
class RegisterAPI(Resource):
    @ns.expect(register_parser)
    def post(self):
        args = register_parser.parse_args()
        username = args['username']
        email = args['email']
        password = args['password']

        user = User.query.filter_by(email=email).first()
        if user:
            return {'message': 'User already exists.'}, 400

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return {'message': 'User registered successfully.', 'data': ns.marshal(new_user, user_model)}, 201

@ns.route('/login')
class LoginAPI(Resource):
    @ns.expect(login_parser)
    def post(self):
        args = login_parser.parse_args()
        email = args['email']
        password = args['password']

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            return {'message': 'User logged in successfully.', 'data': ns.marshal(user, user_model)}, 200

        return {'message': 'Invalid email or password'}, 401