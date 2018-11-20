from base import *

DEBUG = True

# Database
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

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')
STRIPE_SECRET = os.getenv('STRIPE_SECRET')

# Use Django's email backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_ADDRESS')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_PORT = 587