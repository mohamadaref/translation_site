from django.contrib import admin
from django.contrib.auth.admin import  UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from web.models import *

admin.site.register(Client)
admin.site.register(Translator)
admin.site.register(Documents)
admin.site.register(Profile)
# Register your models here.
