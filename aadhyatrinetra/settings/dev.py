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

INSTALLED_APPS += [
    "debug_toolbar",
    "django_browser_reload",
]

# MIDDLEWARE += [
#     "debug_toolbar.middleware.DebugToolbarMiddleware",
#     "django_browser_reload.middleware.BrowserReloadMiddleware",
# ]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1",
]