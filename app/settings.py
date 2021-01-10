from dotenv import load_dotenv
import os

load_dotenv()


HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
DEBUG_STATUS = os.getenv("DEBUG_STATUS")

SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")

# JWT Token Secrete
ACCESS_TOKEN_SECRETE = os.getenv("ACCESS_TOKEN_SECRETE")
REFRESH_TOKEN_SECRETE = os.getenv("REFRESH_TOKEN_SECRETE")

