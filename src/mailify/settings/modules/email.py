from mailify.settings.utils import get_env_variable

ADMINS = (
    ('Biglight', 'heroku@biglight.co.uk'),
)

DEFAULT_FROM_EMAIL = 'Goldsmiths <noreply@mail.goldsmiths.co.uk>'

EMAIL_BACKEND = 'sgbackend.SendGridBackend'
SENDGRID_API_KEY = get_env_variable('SENDGRID_API_KEY')
