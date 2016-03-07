DEBUG = True
SECRET_KEY = 'pindakaas'
ALLOWED_HOSTS = ['*']
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db-name',
        'USER': 'db-user',
        'PASSWORD': 'db-password',
        'HOST': 'localhost',
        'PORT': 5432,
        'CONN_MAX_AGE': 300,  # performance booster 3
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
