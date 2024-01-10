from flask_restx import Resource

from ..extensions import db, ns
from ..models import Column, User, Card
from ..api_models import card_model
from ..parsers import create_card_parser, update_card_parser

@ns.route('/cards')
class CardsAPI(Resource):
    @ns.expect(create_card_parser)
    def post(self):
        args = create_card_parser.parse_args()
        
        column_id = args['columnId']
        column = Column.query.get_or_404(column_id, 'Column not found.')
        
        name = args['name']
        description = args['description']
        
        user_id = args['userId']
        if user_id:
            user = User.query.get_or_404(user_id, 'User not found.')
        
        deadline = args['deadline']

        new_card = Card(column_id=column_id, name=name, description=description, user_id=user_id, deadline=deadline)
        db.session.add(new_card)
        db.session.commit()

        return {'message': 'Card successfully created.', 'data': ns.marshal(new_card, card_model)}, 201

    def get(self):
        all_cards = Card.query.all()
        return {'message': 'Cards retrieved successfully.', 'data': ns.marshal(all_cards, card_model)}

@ns.route('/columns/<int:column_id>/cards')
class CardsByColumnAPI(Resource):
    def get(self, column_id):
        column = Column.query.get_or_404(column_id, 'Column not found.')
        
        all_cards = Card.query.filter_by(column_id=column_id).all()
        return {'message': 'Cards retrieved successfully.', 'data': ns.marshal(all_cards, card_model)}

@ns.route('/cards/<int:card_id>')
class CardAPI(Resource):
    def get(self, card_id):
        card = Card.query.get_or_404(card_id, 'Card not found.')
        return {'message': 'Card retrieved successfully.', 'data': ns.marshal(card, card_model)}

    @ns.expect(update_card_parser)
    def put(self, card_id):
        args = update_card_parser.parse_args()
        card = Card.query.get_or_404(card_id, 'Card not found.')

        if args['columnId']:
            column_id = args['columnId']
            column = Column.query.get_or_404(column_id, 'Column not found.')
            card.column_id = column_id
            
        if args['name']:
            card.name = args['name']
            
        if args['description']:
            card.description = args['description']
            
        
        if args['userId']:
            user_id = args['userId']
            if user_id:
                user = User.query.get_or_404(user_id, 'User not found.')
                card.user_id = user_id
                
        if args['deadline']:
            card.deadline = args['deadline']

        db.session.commit()
        return {'message': 'Card successfully updated.', 'data': ns.marshal(card, card_model)}
    
    def delete(self, card_id):
        card = Card.query.get_or_404(card_id, 'Card not found.')
        db.session.delete(card)
        db.session.commit()
        return '', 204