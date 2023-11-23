import json
import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CRMS.settings")
django.setup()


import jwt
from CRMS.settings import REDIS
from ecom.models import Product
from ecom.utils import Inventory
import arrow

inventory = Inventory()
from dateutil.relativedelta import relativedelta



bb = arrow.get('2023-11-23T10:10:05+00:00').humanize()

print(bb)