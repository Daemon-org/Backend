from django.contrib import admin
from school.models import *

# Register your models here.


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = tuple(field.name for field in Department._meta.fields)
    search_fields = ["department_name", "head_name"]


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = tuple(field.name for field in Subject._meta.fields)
    search_fields = ["subject_name"]


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = tuple(field.name for field in Tutor._meta.fields)
    search_fields = ["full_name"]


@admin.register(Employees)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = tuple(field.name for field in Employees._meta.fields)
    search_fields = ["full_name"]


@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display = tuple(field.name for field in Students._meta.fields)
    search_fields = ["name"]


@admin.register(ClassAttendance)
class ClassAttendanceAdmin(admin.ModelAdmin):
    list_display = tuple(field.name for field in ClassAttendance._meta.fields)
    search_fields = ["student__name"]


@admin.register(StaffAttendance)
class StaffAttendanceAdmin(admin.ModelAdmin):
    list_display = tuple(field.name for field in StaffAttendance._meta.fields)
    search_fields = ["employee__full_name"]


@admin.register(Curriculum)
class CurriculumAdmin(admin.ModelAdmin):
    list_display = tuple(field.name for field in Curriculum._meta.fields)
    search_fields = ["curriculum_name"]


@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = tuple(field.name for field in TimeTable._meta.fields)
    search_fields = ["subject__subject_name"]


@admin.register(StudentFee)
class StudentFeeAdmin(admin.ModelAdmin):
    list_display = tuple(field.name for field in StudentFee._meta.fields)
    search_fields = ["student__name"]


@admin.register(SchoolExpense)
class SchoolExpenseAdmin(admin.ModelAdmin):
    list_display = tuple(field.name for field in SchoolExpense._meta.fields)
    search_fields = ["description", "auth_by"]
