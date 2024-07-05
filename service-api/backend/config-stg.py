from django.conf import settings
from dotenv import load_dotenv
from pathlib import Path
import os

# OR, the same with increased verbosity
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

DEBUG = True
INITDATA = True

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD' : os.getenv("DB_PASSWORD"),
        'HOST' : os.getenv("DB_HOST"),
        'PORT' : os.getenv("DB_PORT"),
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = '/media/'

MONGODB = {
    'USER': os.getenv("MONGODB_USER"),
    'PASSWORD': os.getenv("MONGODB_PASSWORD"),
    'HOST':os.getenv("MONGODB_HOST"),
    'PORT':os.getenv("MONGODB_PORT"),
}


