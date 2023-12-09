import os
from decouple import config
from .settings import *


SECRET_KEY = config('SECRET_KEY')
DEBUG = False

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
CSRF_TRUSTED_ORIGINS = ['https://'+ os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []


hostname = config('DB_HOST')
DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE'),
        'NAME': config('DB_NAME'),
        'HOST': hostname + ".postgres.database.azure.com",
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASS')
    }
}