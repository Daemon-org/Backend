from django.contrib import admin

# Register your models here.
from authentication.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = tuple(field.name for field in Profile._meta.fields)
