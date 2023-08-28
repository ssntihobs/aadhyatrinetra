from .base import *

SECRET_KEY = 'EU9Cpozke$dLCbk2$~byv@fa2amF9$p4~RckzSPi#HZTydQ$NQgZ$ECc29$kugJXD#59YPbmYsZrW59gW@`@k3vVKZVZrLZ43ctK'
ALLOWED_HOSTS = ['impelverse.com', '127.0.0.1']
CSRF_TRUSTED_ORIGINS = ['impelverse.com', '127.0.0.1']
CSRF_ALLOWED_ORIGINS = ["impelverse.com", '127.0.0.1']
CORS_ORIGINS_WHITELIST = ["impelverse.com", '127.0.0.1']

DEBUG = True

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
