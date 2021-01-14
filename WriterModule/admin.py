from django.contrib import admin

from .models import MainTextBody
from .models import UserProfile

# Register your models here.

admin.site.register(MainTextBody)
admin.site.register(UserProfile)