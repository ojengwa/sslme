"""
Django settings for mapoint project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from openssl.config import *
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SITE_ID = 1

ADMINS = [
    ('Bernard', 'bernard@apipanda.com'),
]
MANAGERS = [
    ('Ini', 'ini@apipanda.com'),
]

# Application definition
DEFAULT_FROM_EMAIL = 'support@openssl.io'
SERVER_EMAIL = 'support@openssl.io'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

COMMON_APPS = (
    'apps.api',
    'apps.domain',
    'apps.certificate',

    'tastypie',
    'pinax.blog',
    'social_widgets',
    # 'request',

    # logging
    'slack'

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    # 'request.middleware.RequestMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'openssl.urls'

WSGI_APPLICATION = 'openssl.wsgi.application'


LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/dashboard'
LOGOUT_URL = '/'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DOMAIN_VERIFICATION_OPTIONS = (
    ('C', 'CNAME'),
    ('F', 'File Upload'),
    ('T', 'TXT Record'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/assets/'

MEDIA_URL = '/media/'

# taggit
TAGGIT_CASE_INSENSITIVE = True

TASTYPIE_ALLOW_MISSING_SLASH = True
TASTYPIE_DEFAULT_FORMATS = ['json']
THROTTLE_TIMEOUT = 150
TASTYPIE_API_VERSION = 'v1'


# Twitter
TWITTER_USERNAME = 'openssl_io'
