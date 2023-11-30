from django.urls import path
from school.views import *

urlpatterns = [
    path('get_departments/', get_departments),
    path('add_department/', create_department),
    path('update_department/', update_department),
]
