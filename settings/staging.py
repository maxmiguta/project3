from base import *
import dj_database_url

DEBUG = False
"""
# Local Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'av_db',
        'USER': 'root',
        'PASSWORD': 'dinamo98',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
"""
# Load the ClearDB connection details from the environment variable
DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')
STRIPE_SECRET = os.getenv('STRIPE_SECRET')

# Use Django's email backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'max.miguta@gmail.com'
EMAIL_HOST_PASSWORD = 'blackwolf14'
EMAIL_USE_TLS = True
EMAIL_PORT = 587

SITE_URL = 'https://av-empire.herokuapp.com'
ALLOWED_HOSTS.append('av-empire.herokuapp.com')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
