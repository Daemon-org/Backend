import os
import django
from CRMS.settings import REDIS

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CRMS.settings")
django.setup()

from authentication.utils import Authenticate

auths = Authenticate()
send = auths.send_otp("khemikal2016@gmail.com")


po = auths.get_user_info_from_token("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiODA5NTlkNDItNjUzYy00MTYzLTkzNTctNmM3NzA2OGI0ZTY2IiwiZW1haWwiOiJraGVtaWthbDIwMTZAZ21haWwuY29tIiwiZmlyc3RfbmFtZSI6Ikpvc2giLCJsYXN0X25hbWUiOiJLbmlnaHQiLCJ1c2VybmFtZSI6Impvc2giLCJleHAiOjE3MDAwNDkyNDIuNjEyNjA3LCJpYXQiOjE3MDAwNDgzNDIuNjEyOTI2fQ.FDOAH1k7y5XjQQkpEbWIS4nybf9-ncnu9yONJ0SCx6Q")

print(po)
