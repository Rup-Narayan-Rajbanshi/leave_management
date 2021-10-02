from django.contrib import admin
from leave.models.leave import Leave
from leave.models.leave_request import LeaveRequest
from leave.models.employee_leave import EmployeeLeave
from leave.forms import LeaveRequestForm


class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('employee', 'leave', 'date_from', 'date_to', 'approval_status')
    search_fields = ['employee__first_name','employee__last_name','employee__username']


class EmployeeLeaveAdmin(admin.ModelAdmin):
    list_display = ('employee', 'leave','remaining_leave')
    search_fields = ['employee__first_name','employee__last_name','employee__username']


class LeaveAdmin(admin.ModelAdmin):
    list_display = ('name','no_of_days')

admin.site.register(Leave, LeaveAdmin)
admin.site.register(LeaveRequest, LeaveRequestAdmin)
admin.site.register(EmployeeLeave, EmployeeLeaveAdmin)
