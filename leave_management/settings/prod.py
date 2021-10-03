from .base import *
import os
# from decouple import config

DEBUG = True

ALLOWED_HOSTS = ['rup-leave-tracker.herokuapp.com']

SECRET_KEY = os.environ.get('SECRET_KEY')


DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('NAME'),
        'USER': os.environ.get('USER'),
        'HOST': os.environ.get('HOST'),
        'PORT': os.environ.get('PORT'),
        'PASSWORD':os.environ.get('PASSWORD'),
    }
}


STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),"staticfiles")
STATIC_URL = '/static/'