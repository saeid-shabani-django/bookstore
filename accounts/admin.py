from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserForm,CustomFormAdmin
from .models import CustomUser
class CustomA(UserAdmin):
    add_form = CustomUserForm
    form = CustomFormAdmin
    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields': ('age', )}),
    )
    add_fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', )}),
    )


admin.site.register(CustomUser,CustomA)

