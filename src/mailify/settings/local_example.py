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

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PERMISSION_CLASSES': [],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '15/minute',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SSLIFY_DISABLE = True
