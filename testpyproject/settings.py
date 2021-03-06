"""
Django settings for testpyproject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ROOT_PATH = os.path.dirname(os.path.realpath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$1uw&a%66@uturjv%^wsw)pt6qn!&z(de+9r%s_@=l8wt3tvg3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

PROJECT_APPS = [
    'testpyproject.news',
    'testpyproject.python_game'
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]+PROJECT_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'testpyproject.urls'

WSGI_APPLICATION = 'testpyproject.wsgi.application'

SESSION_COOKIE_DOMAIN = None
SESSION_COOKIE_NAME = "tpp_local_session_id"

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

"""
CREATE DATABASE testprdb CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE USER 'testuser'@localhost IDENTIFIED BY 'testuser';
GRANT ALL PRIVILEGES ON `testprdb`.* TO `testuser`@`localhost`;
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testprdb',
        'USER': 'testuser',
        'PASSWORD': 'testuser',
        'HOST': '',
        'PORT': '3306',
    }
}

TEMPLATE_DIRS = (
    "%s/%s/" % (ROOT_PATH, 'templates'),
)

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '%s/../../static/' % ROOT_PATH

# Additional locations of static files
STATICFILES_MAIN_DIR = '%s/static/' % ROOT_PATH
STATICFILES_DIRS = (
    STATICFILES_MAIN_DIR,
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)