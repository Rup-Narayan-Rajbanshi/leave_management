from django.contrib import admin
from .models import CustomUser
from django.utils.translation import ugettext_lazy as _
from .forms import EmployeeForm


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_superuser')
    form = EmployeeForm
    fieldsets = (
            (_("Personal info"), {
                'fields':(
                    'username', 'email', 'first_name','last_name',\
                     'password'
                    )
                }
            ),
            (_("Employee Status"), {
                'fields':(
                    'is_employee', 'is_superuser','groups'
                    )
                }
            )
            )

admin.site.register(CustomUser, EmployeeAdmin)