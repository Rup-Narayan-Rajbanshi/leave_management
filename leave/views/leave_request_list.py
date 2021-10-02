from django.views.generic import ListView
from leave.models.leave_request import LeaveRequest
from leave.forms import LeaveRequestForm

from django.urls import reverse_lazy, reverse


class LeaveRequestListView(ListView):
    model = LeaveRequest
    template_name = "leave/leave_request_list.html"
    context_object_name = "leave_requests"

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset().filter(employee=user)

        return qs