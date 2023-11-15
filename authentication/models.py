from django.db import models
import uuid


# Create your models here.
class Profile(models.Model):
    email = models.EmailField(unique=True)
    uid = models.UUIDField(default=uuid.uuid4, editable=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True, default="")
    profile_image = models.CharField(max_length=200, blank=True, null=True, default="")
    password = models.CharField(max_length=100, default="")
    username = models.CharField(max_length=100, default="")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    kyc_verified = models.BooleanField(default=False)
    first_login = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    email_verified = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)

    def __str__(self):
        return self.username
