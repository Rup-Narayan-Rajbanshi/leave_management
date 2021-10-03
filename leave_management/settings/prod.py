from .base import *
import os
# from decouple import config

DEBUG = True

ALLOWED_HOSTS = ['rup-leave-tracker.herokuapp.com']

SECRET_KEY = os.environ.get('SECRET_KEY')


DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dftha8tuki4u3l',
        'USER': 'cnzsaytvkrzlda',
        'HOST': 'ec2-34-233-105-94.compute-1.amazonaws.com',
        'PORT': 5432,
        'PASSWORD': '19b36165d253dfaea70deba76b192dbcd2de08cab1aa56d2219440fc5d1a86db',
    }
}


STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),"staticfiles")
STATIC_URL = '/static/'