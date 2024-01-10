from flask_restx import Resource

from ..extensions import db, ns
from ..models import Board, Column
from ..api_models import column_model
from ..parsers import create_column_parser, update_column_parser

@ns.route('/columns')
class ColumnsAPI(Resource):
    @ns.expect(create_column_parser)
    def post(self):
        args = create_column_parser.parse_args()
        board_id = args['boardId']
        board = Board.query.get_or_404(board_id, 'Board not found.')
        
        name = args['name']
        exiting_name = Column.query.filter_by(board_id=board_id, name=name).first()
        if exiting_name:
            return {'message': 'Column name already exists.'}, 400

        new_column = Column(board_id=board_id, name=name)
        db.session.add(new_column)
        db.session.commit()

        return {'message': 'Column successfully created.', 'data': ns.marshal(new_column, column_model)}, 201

    def get(self):
        all_columns = Column.query.all()
        return {'message': 'Columns retrieved successfully.', 'data': ns.marshal(all_columns, column_model)}
    
@ns.route('/boards/<int:board_id>/columns')
class ColumnsByBoardAPI(Resource):
    def get(self, board_id):
        board = Board.query.get_or_404(board_id, 'Board not found.')
        
        all_columns = Column.query.filter_by(board_id=board_id).all()
        return {'message': 'Columns retrieved successfully.', 'data': ns.marshal(all_columns, column_model)}

@ns.route('/columns/<int:column_id>')
class ColumnAPI(Resource):
    def get(self, column_id):
        column = Column.query.get_or_404(column_id, 'Column not found.')
        return {'message': 'Columns retrieved successfully.', 'data': ns.marshal(column, column_model)}

    @ns.expect(update_column_parser)
    def put(self, column_id):
        args = update_column_parser.parse_args()
        column = Column.query.get_or_404(column_id, 'Column not found.')

        if args['name']:
            name = args['name']
            board_id = column.board_id
            exiting_name = Column.query.filter_by(board_id=board_id, name=name).first()
            if exiting_name:
                return {'message': 'Column name already exists.'}, 400
            
            column.name = name

        db.session.commit()
        return {'message': 'Column successfully updated.', 'data': ns.marshal(column, column_model)}
    
    def delete(self, column_id):
        column = Column.query.get_or_404(column_id, 'Column not found.')
        db.session.delete(column)
        db.session.commit()
        return '', 204