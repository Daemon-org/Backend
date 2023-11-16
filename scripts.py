import os
import django
import jwt
from CRMS.settings import REDIS

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CRMS.settings")
django.setup()

from authentication.utils import Authenticate
from decouple import config

auths = Authenticate()
import arrow

code = arrow.now().shift(years=4).datetime
print(code)
