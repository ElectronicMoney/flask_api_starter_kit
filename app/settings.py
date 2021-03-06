from dotenv import load_dotenv
import os

load_dotenv()

API_URL = os.getenv('API_URL')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
DEBUG_STATUS = os.getenv("DEBUG_STATUS")

# Database Credentials Settings
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")

DATABASE_NAME     = os.getenv('DATABASE_NAME')
DATABASE_USER     = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST     = os.getenv('DATABASE_HOST')
DATABASE_PORT     = os.getenv('DATABASE_PORT')

# JWT Token Secrete
ACCESS_TOKEN_SECRETE  = os.getenv("ACCESS_TOKEN_SECRETE")
REFRESH_TOKEN_SECRETE = os.getenv("REFRESH_TOKEN_SECRETE")

# Upload Folder
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")

# TEST_API_TOKEN
TEST_API_TOKEN = os.getenv('TEST_API_TOKEN')