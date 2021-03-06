"""
Django settings for mlproject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%+7_e+m7bvrt4b^up(h_3td*p7y-rmqn+j)^oh9!7emmsv$0kr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mltest',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mlproject.urls'

WSGI_APPLICATION = 'mlproject.wsgi.application'

# Heroku: Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# Heroku: Allow all host headers
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd8j9oauaj55lg9',
        'USER': 'klqzmnaedoevkc',
        'PASSWORD': 'tkBHuxMmGdaAhk7-c0ddFNsUhk',
        'HOST': 'ec2-54-83-204-78.compute-1.amazonaws.com',
        'PORT': '5432',
    },
    'local':  {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pgdb_mlproject',
        'USER': 'deweichen',
        'PASSWORD': 'abcdefgh',
        'HOST': '',
        'PORT': '',
    },
    'sqlite3': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Heroku: db setting
# DATABASES['default'] = dj_database_url.config(default='postgres://klqzmnaedoevkc:tkBHuxMmGdaAhk7-c0ddFNsUhk@ec2-54-83-204-78.compute-1.amazonaws.com:5432/d8j9oauaj55lg9')

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/' # Url to find the static files
STATIC_ROOT = 'staticfiles' # This is where collectstatic collects static files to
STATICFILES_DIRS = (    # Location of all the static files
    os.path.join(BASE_DIR, 'static'),
)

# Templates
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

# Media
MEDIA_URL = '/media/'
MEDIA_ROOT = (
    os.path.join(BASE_DIR, 'media')
)