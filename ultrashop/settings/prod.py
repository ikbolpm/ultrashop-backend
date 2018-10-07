from .base import *
ALLOWED_HOSTS = ['18.208.169.24','ultrashop.uz']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ultrashop',
        'USER': 'ultrashop',
        'PASSWORD': '%ltra$op',
        'HOST': 'localhost',
        'PORT': '5432',

    }
}

WSGI_APPLICATION = 'ultrashop.wsgi_prod.application'

STATIC_ROOT='static'

CORS_ORIGIN_WHITELIST = (
	'ultrashop.uz',
	'www.ultrashop.uz',
	'localhost:8080',
	'127.0.0.1:8080'
)

MEDIA_ROOT = os.path.join(BASE_DIR, '../../media')

BASE_URL = 'http://ultrashop.uz:8000'

DEBUG = True
