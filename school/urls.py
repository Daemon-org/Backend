from django.urls import path
from school.views import *

urlpatterns = [
    path("get_departments/", get_departments),
    path("add_department/", create_department),
    path("update_department/", update_department),
    path("get_employees/", get_employees),
    path("add_employee/", add_employee),
    path("update_employee/", update_employee),
    path("get_subjects/", get_subjects),
    path("add_subject/", add_subjects),
    path("update_subject/", update_subjects),
    path("get_teacher/", get_teachers),
    path("add_teacher/", add_teachers),
    path("update_teacher/", update_teachers),
    path("get_classrooms/", get_classrooms),
    path("add_classroom/", add_classrooms),
    path("update_classroom/", update_classrooms),
    path("get_students/", get_students),
    path("add_student/", add_students),
    path("update_student/", update_students),
    path("class_attendance/", mark_student_attendance),
    path("staff_attendance/", mark_staff_attendance),
]
