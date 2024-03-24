from .base import * #noqa
from .base import env
# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="Yk2sjgky4Ygoj0u6FF6bbzAktxSzN3nlAh83XjcwX_MeofIwIa0",
)


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ['http://localhost:8080']

EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
EMAIL_HOST = env('EMAIL_HOST', default='mailhog')
EMAIL_PORT = env('EMAIL_PORT')
DEFAULT_FROM_EMAIL = 'testdjangoooo@gmail.com'
DOMAIN = env('DOMAIN')
SITE_NAME = 'Authors'
