import os

AUTH_USER_MODEL = "user.User"
ROOT_URLCONF = "rx_verify.urls"
WSGI_APPLICATION = "rx_verify.wsgi.application"

DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
