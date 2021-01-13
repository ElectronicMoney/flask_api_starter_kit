from dotenv import load_dotenv
import os

load_dotenv()

APP_URL = os.getenv('APP_URL')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
DEBUG_STATUS = os.getenv("DEBUG_STATUS")

SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")

# JWT Token Secrete
ACCESS_TOKEN_SECRETE  = os.getenv("ACCESS_TOKEN_SECRETE")
REFRESH_TOKEN_SECRETE = os.getenv("REFRESH_TOKEN_SECRETE")

# Upload Folder
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")

