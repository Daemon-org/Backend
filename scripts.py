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

products = Product.objects.all()

for product in products:
    exp = inventory.check_expiry()
    print(exp.content)

# red = REDIS.get("expiring-products")
# print(json.loads(red))
