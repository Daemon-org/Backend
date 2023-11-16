import os
import django
import jwt
from CRMS.settings import REDIS

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CRMS.settings")
django.setup()

from authentication.utils import Authenticate
from decouple import config
import string
import random


def gen_otp():
    letters = string.digits
    return "".join(random.choice(letters) for _ in range(5))


def generate_otp(self):
    # Generate a random 5-digit OTP
    return random.randint(10000, 99999)
