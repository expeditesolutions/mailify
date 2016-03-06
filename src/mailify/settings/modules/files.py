import os
from mailify.settings.utils import PROJECT_DIR


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

FAVICON_PATH = STATIC_URL + 'images/favicon.png'
