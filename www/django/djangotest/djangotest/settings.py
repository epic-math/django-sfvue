"""
Django settings for djangotest project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b4b98$vjk+j7aseci27n3*9)rky36o+-bz3vh6=z6q^p3*0z+)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# provide our get_profile()
AUTH_PROFILE_MODULE = 'driver.Driver'

# Application definition
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'car',
    'tinymce',
    'pages',
    'driver',
    'custom_facebook_tab',
    'django.contrib.admin',
    'social.apps.django_app.default', 
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'djangotest.urls'


#TEMPLATE_DIRS = (
#     	'/srv/www/django/djangotest/djangotest/templates/',
#)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangotest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangotestdb',
        'USER': 'djangotestuser',
        'PASSWORD': 'K3zHqeArA9S5v3DR',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/srv/www/djangotest.sfvue.com/public_html/static'
MEDIA_ROOT = '/srv/www/djangotest.sfvue.com/public_html/media'
MEDIA_URL = '/media/'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'kihyuck.hong@gmail.com'
EMAIL_HOST_PASSWORD = 'idaho21G'
EMAIL_HOST_PASSWORD = 'tlwfanckvguholmb'
EMAIL_PORT = 587


# URL for @login_required decorator 
LOGIN_URL = '/login/'

# redirect authenticated users
LOGIN_REDIRECT_URL = '/profile/'


SOCIAL_AUTH_FACEBOOK_KEY = '940636552659697'
SOCIAL_AUTH_FACEBOOK_SECRET = '7e4558141d870c597efc5736fb656e1d'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '158622460441-qv7qkqibptp07el3rpf1osk3qfrv8ddu.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '4aFCTaLI-d7Dwv39MgW2bLQh'

SOCIAL_AUTH_TWITTER_KEY = 'QCqEYFv4B1RdymvkNDa1iveJ8'
SOCIAL_AUTH_TWITTER_SECRET = 'Dx1f88oaJQwY2IaRJRMFzQ0FLYwl1613kCfuYVRwhT3aLbM3Cy'
