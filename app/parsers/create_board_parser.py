from flask_restx import reqparse

create_board_parser = reqparse.RequestParser()
create_board_parser.add_argument('name', type=str, required=True, help='Name')
create_board_parser.add_argument('description', type=str, help='Description')