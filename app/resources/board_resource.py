from flask_restx import Resource

from ..extensions import db, ns
from ..models import Board
from ..api_models import board_model
from ..parsers import create_board_parser, update_board_parser

@ns.route('/boards')
class BoardsAPI(Resource):
    @ns.expect(create_board_parser)
    def post(self):
        args = create_board_parser.parse_args()
        name = args['name']
        description = args['description']

        new_board = Board(name=name, description=description)
        db.session.add(new_board)
        db.session.commit()

        return {'message': 'Board successfully created.', 'data': ns.marshal(new_board, board_model)}, 201

    def get(self):
        all_boards = Board.query.all()
        return {'message': 'Boards retrieved successfully.', 'data': ns.marshal(all_boards, board_model)}
    

@ns.route('/boards/<int:board_id>')
class BoardAPI(Resource):
    def get(self, board_id):
        board = Board.query.get_or_404(board_id, 'Board not found.')
        return {'message': 'Board retrieved successfully.', 'data': ns.marshal(board, board_model)}

    @ns.expect(update_board_parser)
    def put(self, board_id):
        args = update_board_parser.parse_args()
        board = Board.query.get_or_404(board_id, 'Board not found.')

        if args['name']:
            board.name = args['name']
        if args['description']:
            board.description = args['description']

        db.session.commit()
        return {'message': 'Board successfully updated.', 'data': ns.marshal(board, board_model)}
    
    def delete(self, board_id):
        board = Board.query.get_or_404(board_id, 'Board not found.')
        db.session.delete(board)
        db.session.commit()
        return '', 204