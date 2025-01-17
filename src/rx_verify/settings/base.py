import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DEBUG = os.environ.get("DEBUG")

SECRET_KEY = os.environ.get("SECRET_KEY")
REFRESH_TOKEN_SECRET = os.environ.get("REFRESH_TOKEN_SECRET")

ALLOWED_HOSTS = ["*"]
