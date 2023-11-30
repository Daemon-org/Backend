import json
from django.shortcuts import render
from django.http import JsonResponse
from CRMS.decorators import check_fields, token_required
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt
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


@csrf_exempt
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

@csrf_exempt
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
        update = admit.update_department(department_id, name, role, head_name)
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

@csrf_exempt
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

@csrf_exempt
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
        update = admit.update_employee(employee_id,full_name, department, status)
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

@csrf_exempt
@require_POST
@token_required
@check_fields(["name", "description"])
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

@csrf_exempt
@require_POST
@token_required
@check_fields(["subject_id"])
def update_subjects(request):
    try:
        data = json.loads(request.body)
        subject_id = data.get("subject_id")
        name = data.get("name")
        description = data.get("description")

        sub = admit.update_subject(
            subject_id=subject_id, name=name, description=description
        )
        return sub
    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})


@require_GET
def get_teachers(request):
    try:
        teachers = admit.get_tutors()
        return teachers
    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})

@csrf_exempt
@require_POST
@token_required
@check_fields(["full_name", "subjects", "department_id"])
def add_teachers(request):
    try:
        data = json.loads(request.body)
        full_name = data.get("full_name")
        subjects = data.get("subjects")
        department_id = data.get("department_id")

        sub = admit.add_teacher(full_name, subjects, department_id)
        return sub
    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})

@csrf_exempt
@require_POST
@token_required
@check_fields(["tutor_id"])
def update_teachers(request):
    try:
        data = json.loads(request.body)
        tutor_id = data.get("tutor_id")
        full_name = data.get("full_name")
        subjects = data.get("subjects")

        sub = admit.update_tutor(tutor_id, full_name, subjects)
        return sub
    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})


@require_GET
def get_classrooms(request):
    try:
        classrooms = admit.get_classrooms()
        return classrooms
    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})

@csrf_exempt
@require_POST
@token_required
@check_fields(["teacher_id", "grade", "capacity"])
def add_classrooms(request):
    try:
        data = json.loads(request.body)
        teacher_id = data.get("teacher_id")
        grade = data.get("grade")
        capacity = data.get("capacity")

        sub = admit.add_classroom(teacher_id, grade, capacity)
        return sub
    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})

@csrf_exempt
@require_POST
@token_required
@check_fields(["classroom_id"])
def update_classrooms(request):
    try:
        data = json.loads(request.body)
        classroom_id = data.get("classroom_id")
        teacher_id = data.get("teacher_id")
        grade = data.get("grade")
        capacity = data.get("capacity")

        sub = admit.update_classroom(classroom_id, teacher_id, grade, capacity)
        return sub
    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})


@require_GET
def get_students(request):
    try:
        students = admit.get_students()
        return students
    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})

@csrf_exempt
@require_POST
@token_required
@check_fields(
    [
        "name",
        "age",
        "gender",
        "address",
        "classroom_id",
        "parent_name",
        "p_phone",
        "p_email",
    ]
)
def add_students(request):
    try:
        data = json.loads(request.body)
        name = data.get("name")
        age = data.get("age")
        gender = data.get("gender")
        address = data.get("address")
        classroom_id = data.get("classroom_id")
        parent_name = data.get("parent_name")
        p_phone = data.get("p_phone")
        p_email = data.get("p_email")

        sub = admit.add_student(
            name, age, gender, address, classroom_id, parent_name, p_phone, p_email
        )
        return sub
    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})

@csrf_exempt
@require_POST
@token_required
@check_fields(["student_id"])
def update_students(request):
    try:
        data = json.loads(request.body)
        student_id = data.get("student_id")
        name = data.get("name")
        age = data.get("age")
        gender = data.get("gender")
        address = data.get("address")
        classroom_id = data.get("classroom_id")
        parent_name = data.get("parent_name")
        p_phone = data.get("p_phone")
        p_email = data.get("p_email")
        status = data.get("status")

        sub = admit.update_student(
            student_id,
            name,
            age,
            gender,
            address,
            classroom_id,
            parent_name,
            p_phone,
            p_email,
            status,
        )
        return sub
    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})

@csrf_exempt
@require_POST
@token_required
@check_fields(["student_id", "class_room", "status"])
def mark_student_attendance(request):
    try:
        data = json.loads(request.body)
        student_id = data.get("student_id")
        class_room = data.get("class_room")
        status = data.get("status")

        sub = admit.mark_class_attendance(student_id, class_room, status)
        return sub
    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})

@csrf_exempt
@require_POST
@token_required
@check_fields(["employee", "department"])
def mark_staff_attendance(request):
    try:
        data = json.loads(request.body)
        employee = data.get("employee")
        department = data.get("department")

        sub = admit.mark_staff_attendance(employee, department)
        return sub
    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})
