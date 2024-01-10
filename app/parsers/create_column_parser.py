from flask_restx import reqparse

create_column_parser = reqparse.RequestParser()
create_column_parser.add_argument('boardId', type=int, required=True, help='Board ID')
create_column_parser.add_argument('name', type=str, required=True, help='Name')