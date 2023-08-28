from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "^LC^&vb`K&rL9eYRr&MV9yc^YyjF&2npAJYDhv&qa5J9TgvnCEwj`C7^#5VxQqQ%Cih3ieQ#eNZ`z&d3b`prjLo`nwFe`cMQXwXo"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .base import *
except ImportError:
    pass

TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1",
]