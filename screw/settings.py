"""
Django settings for screw_test project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import sys
import os

# set python path
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_PATH)

# Template path, static path
TEMPLATES_PATH, STATIC_PATH = map(lambda x: os.path.join(PROJECT_PATH, x).replace('\\', '/'), ('templates/', 'static/'))

import pymongo
from mongoengine import connect
from django.conf import global_settings
from screw.config import *

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

mongo_client = connect(MONGODB_NAME, host=MONGODB_DATABASE_HOST)
#mongo_client.screw.authenticate((MONGODB_USER, MONGODB_PASSWD), source='admin')


TEMPLATE_DEBUG = DEBUG

# mongoengine auth settings
AUTH_USER_MODAL = 'mongo_auth.MongoUser'
MONGOENGINE_USER_DOCUMENT = 'mongoengine.django.auth.User'

AUTHENTICATION_BACKENDS = (
    'mongoengine.django.auth.MongoEngineBackend',
)

# mongoengine sessions settings
SESSION_ENGINE = 'mongoengine.django.sessions'
SESSION_SERIALIZER = 'mongoengine.django.sessions.BSONSerializer'
SESSION_COOKIE_AGE = 60 * 60 * 8
SESSION_COOKIE_NAME = 'screw_sid'
SESSION_COOKIE_DOMAIN = '.screw.com.cn'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# static path or url
if os.path.exists('%s/.git' % PROJECT_PATH):
    STATIC_URL = '/static/'
else:
    STATIC_URL = 'http://static.screw.com.cn/static/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n8v(8pe#$(#8z2ck2p6i+lmbeovtvh+f$)hu2wbp6d#4ufyi&q'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'screw',
    'screw.app.good',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'screw.urls'

WSGI_APPLICATION = 'screw.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = 'zh-hans'

USE_I18N = True

USE_L10N = True

USE_TZ = True
