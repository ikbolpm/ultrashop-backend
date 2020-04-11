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

STATIC_ROOT= os.path.join(BASE_DIR, '../../static')

CORS_ORIGIN_WHITELIST = (
	'ultrashop.uz',
	'www.ultrashop.uz',
    'https://ultrashop.uz',
)

MEDIA_ROOT = os.path.join(BASE_DIR, '../../media')
DEBUG = False