import os
import django
from CRMS.settings import REDIS

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CRMS.settings")
django.setup()

from authentication.utils import Authenticate

auths = Authenticate()
send = auths.send_otp("khemikal2016@gmail.com")
print(send.content)

po = REDIS.get("khemikal2016@gmail.com")

print(po)
