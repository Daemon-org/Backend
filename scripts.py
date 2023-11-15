import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CRMS.settings")
django.setup()

print("Starting script...")