from __future__ import absolute_import
import os

from .settings import *  # noqa

if os.environ['DB'] == 'sqlite':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'test_db',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'test_ool',
            'USER': 'postgres'
        }
    }
