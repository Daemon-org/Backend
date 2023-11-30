import json
from django.shortcuts import render
from django.http import JsonResponse
from CRMS.decorators import check_fields,token_required
from django.views.decorators.http import require_POST, require_GET
import logging
logger = logging.getLogger(__name__)

# Create your views here.
from school.utils import Admitter

admit = Admitter()

def get_departments(request):
    try:
        departments = admit.get_departments()
        return departments
    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})
    
@token_required
@require_POST
@check_fields(["name", "role", "head_name"])
def create_department(request):
    try:
       data = json.loads(request.body)
       name = data.get("name")
       role = data.get("role")
       head_name = data.get("head_name")

       add = admit.add_department(name, role, head_name)
       return add
    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})


@require_POST
@token_required
def update_department(request):
    try:
        data = json.loads(request.body)
        name = data.get("name")
        role = data.get("role")
        head_name = data.get("head_name")
        update = admit.update_department(name, role, head_name)
        return update
    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})
