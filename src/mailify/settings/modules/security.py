from mailify.settings.utils import get_env_variable


SECRET_KEY = get_env_variable('SECRET_KEY')

ALLOWED_HOSTS = ['mailify.webdesignwill.io', ]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
