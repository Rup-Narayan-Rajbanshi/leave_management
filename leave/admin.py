from django.contrib import admin
from leave.models.leave import Leave
from leave.models.leave_request import LeaveRequest
from leave.models.employee_leave import EmployeeLeave
from leave.models.leave_approval import LeaveApproval
from leave.forms import LeaveRequestForm


class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('employee', 'leave', 'date_from', 'date_to', 'approval_status')
    # form = LeaveRequestForm


class EmployeeLeaveAdmin(admin.ModelAdmin):
    list_display = ('employee', 'leave', 'remaining_leave')


class LeaveApprovalAdmin(admin.ModelAdmin):
    list_display = ('leave_request', 'approval_status')


admin.site.register(Leave)
admin.site.register(LeaveRequest, LeaveRequestAdmin)
admin.site.register(EmployeeLeave, EmployeeLeaveAdmin)
admin.site.register(LeaveApproval, LeaveApprovalAdmin)
