from django.contrib import admin
from .forms import UserCustomChangeForm, UserCustomCreationForm
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAmin(UserAdmin):
    add_form = UserCustomCreationForm
    form = UserCustomChangeForm
    model = CustomUser 
    list_display = ['email','username','age','is_staff',]


admin.site.register(CustomUser,CustomUserAmin)