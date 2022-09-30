from .common import *


SECRET_KEY = 'django-insecure-hs6j037urx6iav+7#10%-vu4l4f5@@-1_zo)oft4g7$vf2$jmp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront3',
        'HOST': 'mysql',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}

if DEBUG:
    MIDDLEWARE += ['silk.middleware.SilkyMiddleware']


EMAIL_BACKEND= 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST= 'smtp4dev'
EMAIL_HOST_USER= ''
EMAIL_HOST_PASSWORD= ''
EMAIL_PORT= 2525
DEFAULT_FROM_EMAIL= 'from@buy.com'

ADMINS = [
    ('Rhx', 'admin@buy.com')
]

CELERY_BROKER_URL = 'redis://redis:6379/1'
CELERY_BEAT_SCHEDULE= {
    'notify_customers' : {
        'task' : 'playground.tasks.notify_customers',
        'schedule' : 5,
        'args' : ['Hello World']
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK' : lambda request : True
}