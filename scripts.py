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


exp = inventory.sales_analytics()
print(exp.content)
