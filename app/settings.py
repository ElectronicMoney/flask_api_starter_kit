from dotenv import load_dotenv
import os

load_dotenv()


PORT = os.getenv('PORT')
DEBUG_STATUS = os.getenv("DEBUG_STATUS")

SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")

