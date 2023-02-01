from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
# Register your models here.

class MyUserAdmin(UserAdmin):
    readonly_fields = ('created_at', 'last_logged_in')
    list_display = ('email', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password','username')}),
        (('Personal info'), {
         'fields': ('first_name', 'last_name', 'mobile_number')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                      'groups')}),
        (('Important dates'), {'fields': ('created_at', 'last_logged_in')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    form = UserChangeForm
    add_form = UserCreationForm

admin.site.register(User,MyUserAdmin)
