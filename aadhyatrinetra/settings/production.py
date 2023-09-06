from .base import *

SECRET_KEY = 'EU9Cpozke$dLCbk2$~byv@fa2amF9$p4~RckzSPi#HZTydQ$NQgZ$ECc29$kugJXD#59YPbmYsZrW59gW@`@k3vVKZVZrLZ43ctK'
ALLOWED_HOSTS = ['impelverse.com', '143.110.244.126']
CSRF_TRUSTED_ORIGINS = ['impelverse.com', '143.110.244.126']
CSRF_ALLOWED_ORIGINS = ["impelverse.com", '143.110.244.126']
CORS_ORIGINS_WHITELIST = ["impelverse.com", '143.110.244.126']

DEBUG = True

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
