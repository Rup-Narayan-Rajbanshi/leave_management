from helpers.mixins import GroupRequiredMixin
from leave.models.leave_request import LeaveRequest
from leave.models.employee_leave import EmployeeLeave

from django.contrib.auth.decorators import login_required
from django.views.generic import ListView


class LeaveRequestListView(GroupRequiredMixin, ListView):
    """
    View to list all the leave requests and Allocated leave of a loggedin user
    """
    model = LeaveRequest
    template_name = "leave/leave_request_list.html"

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset().filter(employee=user)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        leave_requests = self.get_queryset()
        allocated_leaves = EmployeeLeave.objects.filter(employee=self.request.user)

        context = {
            'leave_requests': leave_requests,
            'allocated_leaves': allocated_leaves
        }
        return context