import os
import dj_database_url
from .commonsettings import *


DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['taskmate-2-kxfe.onrender.com', 'localhost']

CORS_ALLOWED_ORIGINS = [
    "https://sylwambani.github.io",
    "https://taskmate-2-kxfe.onrender.com",
]


DATABASES = {
    'default': dj_database_url.config(
        default=os.environ['DATABASE_URL'],
        conn_max_age=600,
        ssl_require=True
    )
}

CSRF_TRUSTED_ORIGINS = [
    "https://sylwambani.github.io",
    "https://taskmate-2-kxfe.onrender.com",
]

SECURE_CROSS_ORIGIN_OPENER_POLICY = None
