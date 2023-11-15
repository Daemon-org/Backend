from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from CRMS.decorators import check_fields
from authentication.utils import Authenticate
from django.contrib.auth import login, logout
from authentication.models import Profile
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.hashers import check_password

import logging

logger = logging.getLogger(__name__)


auth = Authenticate()


@check_fields(
    ["username", "email", "first_name", "last_name", "phone_number", "password"]
)
@csrf_exempt
@require_POST
def register_user(request):
    try:
        data = json.loads(request.body)
        username = data.get("username")
        email = data.get("email")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        phone_number = data.get("phone_number")
        password = data.get("password")
        auth.register_user(
            username, email, first_name, last_name, phone_number, password
        )
    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})


@check_fields(["email", "password"])
@csrf_exempt
@require_POST
def login_user(request):
    try:
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")
        auth.login_user(email, password)
    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})
