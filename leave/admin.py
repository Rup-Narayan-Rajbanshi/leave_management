from django.contrib import admin
from leave.models import Leave, LeaveRequest, EmployeeLeave

# Register your models here.
admin.site.register(Leave)
admin.site.register(LeaveRequest)
admin.site.register(EmployeeLeave)
