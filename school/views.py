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

@require_GET
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
@check_fields(["department_id"])
def update_department(request):
    try:
        data = json.loads(request.body)
        department_id = data.get("department_id")
        name = data.get("name")
        role = data.get("role")
        head_name = data.get("head_name")
        update = admit.update_department(department_id,name, role, head_name)
        return update
    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})

@require_GET
def get_employees(request):
    try:
        employees = admit.get_employees()
        return employees
    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})

@require_POST
@token_required
@check_fields(["full_name", "department"])
def add_employee(request):
    try:
        data = json.loads(request.body)
        full_name = data.get("full_name")
        department = data.get("department")

        add = admit.add_employee(full_name, department)
        return add
    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})
    

@require_POST
@token_required
@check_fields(["employee_id"])
def update_employee(request):
    try:
        data = json.loads(request.body)
        employee_id = data.get("employee_id")
        full_name = data.get("full_name")
        department = data.get("department")
        status = data.get("status")
        update = admit.update_employee(full_name, department,status)
        return update
    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})
    

@require_GET
def get_subjects(request):
    try:
        subjects = admit.get_subjects()
        return subjects
    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})
    

@require_POST
@token_required
@check_fields(["name","description"])
def add_subjects(request):
    try:
        data = json.loads(request.body)
        name = data.get("name")
        description = data.get("description")
        
        sub = admit.add_subjects(name, description)
        return sub
    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})
    

@require_POST
@token_required
@check_fields(["subject_id"])
def update_subjects(request):
    try:
        data = json.loads(request.body)
        subject_id = data.get("subject_id")
        name = data.get("name")
        description = data.get("description")
        
        sub = admit.update_subject(subject_id=subject_id, name=name, description=description)
        return sub
    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})
    

