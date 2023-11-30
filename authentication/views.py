from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from CRMS.decorators import check_fields, token_required
from authentication.utils import Authenticate
from django.contrib.auth import logout
from authentication.models import Profile
from django.views.decorators.http import require_POST, require_GET

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
        reg = auth.register_user(
            username, email, first_name, last_name, phone_number, password
        )
        return reg
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
        log = auth.login_user(email, password, request)
        return log
    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})


@check_fields(["email", "otp_code"])
@csrf_exempt
@require_POST
def verify_email(request):
    try:
        data = json.loads(request.body)
        email = data.get("email")
        otp_code = data.get("otp_code")

        return auth.verify_otp(
            email,
            otp_code,
        )
    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})


@token_required
@require_GET
def get_profiles(request):
    try:
        profiles = Profile.objects.all()
        return JsonResponse({"success": True, "data": list(profiles.values())})
    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})


@require_POST
@csrf_exempt
@token_required
def logout_user(request):
    logout(request)
    return JsonResponse({"success": True, "info": "Logged out successfully."})
