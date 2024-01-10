from flask_restx import reqparse

update_column_parser = reqparse.RequestParser()
update_column_parser.add_argument('name', type=str, help='Name')