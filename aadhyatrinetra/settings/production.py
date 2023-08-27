from .base import *

SECRET_KEY = 'EU9Cpozke$dLCbk2$~byv@fa2amF9$p4~RckzSPi#HZTydQ$NQgZ$ECc29$kugJXD#59YPbmYsZrW59gW@`@k3vVKZVZrLZ43ctK'
ALLOWED_HOSTS = ['https://*.impelverse.com', 'https://*.127.0.0.1']
CSRF_TRUSTED_ORIGINS = ['https://*.impelverse.com', 'https://*.127.0.0.1']

DEBUG = False

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
