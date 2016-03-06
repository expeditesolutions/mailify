DEBUG = True
SECRET_KEY = 'alj8p4%@vmx6+z!#u%2d_@5#lcs2$4ehx&-il4m&5sgp9dv-6&'
ALLOWED_HOSTS = ['*']
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mailify_dev',
        'USER': 'michael',
        'PASSWORD': 'my5q1',
        'HOST': 'localhost',
        'PORT': 5432,
        'CONN_MAX_AGE': 300,  # performance booster 3
    }
}
