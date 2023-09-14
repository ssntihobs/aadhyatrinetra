from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = str(os.getenv('SECRET_KEY'))
ALLOWED_HOSTS = ['impelverse.com', '139.59.86.210']
CSRF_TRUSTED_ORIGINS = ['impelverse.com', '139.59.86.210']
CSRF_ALLOWED_ORIGINS = ["impelverse.com", '139.59.86.210']
CORS_ORIGINS_WHITELIST = ["impelverse.com", '139.59.86.210']

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": str(os.getenv('DB_NAME')),
        "USER": str(os.getenv('DB_USER')),
        "PASSWORD": str(os.getenv('DB_PASSWORD')),
        'HOST': str(os.getenv('DB_HOST')),
        'PORT': str(os.getenv('DB_PORT')),
    }
}

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
