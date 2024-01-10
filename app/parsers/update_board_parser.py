from flask_restx import reqparse

update_board_parser = reqparse.RequestParser()
update_board_parser.add_argument('name', type=str, help='Name')
update_board_parser.add_argument('description', type=str, help='Description')