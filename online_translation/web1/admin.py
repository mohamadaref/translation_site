from django.contrib import admin
from django.contrib.auth import get_user_model
from web1.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from web1.models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'ProfileImage']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Client)
admin.site.register(Translator)
admin.site.register(Document)
# Register your models here.
