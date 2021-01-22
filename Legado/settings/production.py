from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'legado', 
        'USER': 'root',
        'PASSWORD': 'Skua0748',
        'HOST': 'localhost',
        'PORT': '3306',
    }
    
}