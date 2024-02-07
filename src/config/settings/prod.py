import os

from config.settings.base import *  # NOQA

DEBUG = False

SECRET_KEY = os.getenv("SECRET_KEY")

ALLOWED_HOSTS = []

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR.parent / "static/"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR.parent / "media/"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": os.getenv("POSTGRES_PORT"),
    }
}

WSGI_APPLICATION = "config.wsgi.application"
