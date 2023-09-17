from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

SECRET_KEY = str(os.getenv('SECRET_KEY'))
ALLOWED_HOSTS = ['www.impelverse.com', '139.59.86.210']
CSRF_TRUSTED_ORIGINS = ['www.impelverse.com', '139.59.86.210']
# CSRF_ALLOWED_ORIGINS = ["www.impelverse.com", '139.59.86.210']
# CORS_ORIGINS_WHITELIST = ["www.impelverse.com", '139.59.86.210']
DJANGO_SETTINGS_MODULE = os.environ.get('DJANGO_SETTINGS_MODULE')

DEBUG = True

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Application definition

INSTALLED_APPS = [

    "categories",
    "blogs",
    "wagtailmarkdown",

    "tailwind",
    "theme",

    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail.contrib.routable_page",
    "wagtail",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django.contrib.sitemaps',
    "wagtailmetadata",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = "aadhyatrinetra.urls"

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

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "blogs.context_preprocessors.blog_page",
                "blogs.context_preprocessors.categories",
            ],
        },
    },
]

WSGI_APPLICATION = "aadhyatrinetra.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

WAGTAIL_I18N_ENABLED = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
]

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/4.2/ref/contrib/staticfiles/#manifeststaticfilesstorage
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

STATICFILES_HEADERS = {
    'Cache-Control': 'public, max-age=31536000',  # Cache for one year
}

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# Wagtail settings

WAGTAIL_SITE_NAME = "aadhyatrinetra"

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-prefix',
    }
}

# Cache duration for static files (in seconds)
# Adjust this value based on your needs
CACHE_CONTROL_MAX_AGE = 3600  # 1 hour

# Search
# https://docs.wagtail.org/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = "https://www.impelverse.com"

WAGTAILIMAGES_IMAGE_MODEL = "blogs.CustomImage"

WAGTAIL_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.extra',
    'markdown.extensions.codehilite',
    'blogs.markdown_extensions',
    # Add any other extensions you need
]

WAGTAILMARKDOWN = {
    "autodownload_fontawesome": False,
    "allowed_tags": [],  # optional. a list of HTML tags. e.g. ['div', 'p', 'a']
    "allowed_styles": [],  # optional. a list of styles
    "allowed_attributes": {},  # optional. a dict with HTML tag as key and a list of attributes as value
    "allowed_settings_mode": "extend",  # optional. Possible values: "extend" or "override". Defaults to "extend".
    "extensions": [],  # optional. a list of python-markdown supported extensions
    "extension_configs": {},  # optional. a dictionary with the extension name as key, and its configuration as value
    "extensions_settings_mode": "extend",  # optional. Possible values: "extend" or "override". Defaults to "extend".
}

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
