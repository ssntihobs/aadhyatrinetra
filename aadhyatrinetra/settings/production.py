from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = str(os.getenv('SECRET_KEY'))
ALLOWED_HOSTS = ['impelverse.com', '143.110.244.126']
CSRF_TRUSTED_ORIGINS = ['impelverse.com', '143.110.244.126']
CSRF_ALLOWED_ORIGINS = ["impelverse.com", '143.110.244.126']
CORS_ORIGINS_WHITELIST = ["impelverse.com", '143.110.244.126']

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
