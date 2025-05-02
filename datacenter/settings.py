from dotenv import load_dotenv
import os

load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.getenv('DB_HOST'),
        'PORT': '5434',
        'NAME': 'checkpoint',
        'USER': 'guard',
        'PASSWORD': os.getenv('DB_PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv('APP_SECRET_KEY')

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
