from .base import *
from decouple import config

DEBUG = True

ALLOWED_HOSTS = ['*']

SECRET_KEY = config('SECRET_KEY')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "staticfiles"),
    # '/var/www/static/',
]

STATIC_ROOT=os.path.join(os.path.dirname(BASE_DIR),"static_root")

MEDIA_URL= '/media/'
 
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),"media_root")
