ALLOWED_HOSTS = ['18.208.169.24']

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

CORS_ORIGIN_WHITELIST = 'localhost:8080'

BASE_URL = 'http://localhost:8000'
