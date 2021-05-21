#------------------------------------------------------------------------------
# This file will only be actioned when the site is run from the local test
# server. When run from a live server, this file will not be present and so
# the settings in the main settings.py file will be actioned.
#------------------------------------------------------------------------------
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

STATICFILES_DIRS = [BASE_DIR / 'static',]
STATIC_ROOT = None
