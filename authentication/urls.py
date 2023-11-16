from django.urls import path
from authentication.views import *

urlpatterns = [
    path("login/", login_user),
    path("register/", register_user),
    path("verify/", verify_email),
    path("profiles/", get_profiles),
    path("logout/", logout_user),
]
