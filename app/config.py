from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    def __init__(self):
        self.SQLALCHEMY_DATABASE_URI=os.getenv("SQLALCHEMY_DATABASE_URI")
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False

config = Config()