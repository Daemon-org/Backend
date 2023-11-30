from django.urls import path
from school.views import *

urlpatterns = [
    path('get_departments/', get_departments),
    path('add_department/', create_department),
    path('update_department/', update_department),
    path('get_employees/', get_employees),
    path('add_employee/', add_employee),
    path('update_employee/', update_employee),
    path('get_subjects/', get_subjects),
    path('add_subject/', add_subjects),
    path('update_subject/', update_subjects),
    
]
