from .base import *

DEBUG = False
SECRET_KEY = "django-insecure-86f!dgt8^=8cj6ts+u!whmf85&ldb5=3%g80z2y(ls+2#*cfdx"
ALLOWED_HOSTS = ["*"]

try:
    from .base import *
except ImportError:
    pass
