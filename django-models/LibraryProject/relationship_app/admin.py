from django.contrib import admin

# Register your models here.
# relationship_app/admin.py

from .models import Profile

admin.site.register(Profile)