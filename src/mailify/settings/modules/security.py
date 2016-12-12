import datetime
from mailify.settings.utils import get_env_variable


SECRET_KEY = get_env_variable('SECRET_KEY')

ALLOWED_HOSTS = ['mailify.herokuapp.com', 'mailify-1.herokuapp.com', 'mailify-2.herokuapp.com', 'mailify-3.herokuapp.com', 'mailify-4.herokuapp.com', 'mailify-5.herokuapp.com', 'mailify-6.herokuapp.com', 'mailify-7.herokuapp.com', 'mailify-8.herokuapp.com', 'mailify-9.herokuapp.com', 'mailify-10.herokuapp.com', 'mailify-1.herokuapp.com',]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Axes is for preventing brute force on the login
AXES_LOGIN_FAILURE_LIMIT = 5

# If set, defines a period of inactivity after which old failed login attempts will be forgotten. Can be set to a python timedelta object or an integer. If an integer, will be interpreted as a number of hours.
AXES_COOLOFF_TIME = datetime.timedelta(minutes=15)
AXES_LOCKOUT_TEMPLATE = 'lockout.html'

CORS_ORIGIN_ALLOW_ALL = True
