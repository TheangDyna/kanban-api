from flask_restx import reqparse
from datetime import datetime

create_card_parser = reqparse.RequestParser()
create_card_parser.add_argument('columnId', type=int, required=True, help='Colum ID')
create_card_parser.add_argument('name', type=str, required=True, help='Name')
create_card_parser.add_argument('description', type=str, help='Description')
create_card_parser.add_argument('userId', type=int, help='User ID')
create_card_parser.add_argument('deadline', type=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S') if x else None, help='Deadline')