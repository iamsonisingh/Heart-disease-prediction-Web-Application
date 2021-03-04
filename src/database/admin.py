from django.contrib import admin

# Register your models here.

from .models import userInfo, user

admin.site.register(userInfo)
admin.site.register(user)
