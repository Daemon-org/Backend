import os
import django
import jwt
from CRMS.settings import REDIS

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CRMS.settings")
django.setup()

from authentication.utils import Authenticate
from decouple import config

auths = Authenticate()

code = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNDg2NzBkMDgtZDQwNy00NzA3LWFkMTgtZDgyNzE4MmY5ZDdlIiwiZW1haWwiOiJraGVtaWthbDIwMTZAZ21haWwuY29tIiwiZmlyc3RfbmFtZSI6Ikpvc2giLCJsYXN0X25hbWUiOiJLbmlnaHQiLCJ1c2VybmFtZSI6Impvc2giLCJleHAiOjE3MDAwNTgzNTMuODYxMDUyLCJpYXQiOjE3MDAwNTc0NTMuODYxMzA2LCJ0b2tlbl90eXBlIjoiYWNjZXNzIn0.n8rtU_i89MR0q_nogJLQ86Sle_VhypYpXRCOrch51bI"
po = jwt.decode(code,config("SECRET_KEY"), algorithms=["HS256"])

print(po)
