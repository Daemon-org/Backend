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


# exp = inventory.check_expiration()
# print(exp)

red = REDIS.get("almost-expired-products")
print(json.loads(red))
