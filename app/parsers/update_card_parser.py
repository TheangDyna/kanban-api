from flask_restx import reqparse
from datetime import datetime

update_card_parser = reqparse.RequestParser()
update_card_parser.add_argument('columnId', type=int, help='Colum ID')
update_card_parser.add_argument('name', type=str, help='Name')
update_card_parser.add_argument('description', type=str, help='Description')
update_card_parser.add_argument('userId', type=int, help='User ID')
update_card_parser.add_argument('deadline', type=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S') if x else None, help='deadline')