from helpers.mixins import GroupRequiredMixin
from leave.models.leave_request import LeaveRequest
from leave.forms import LeaveRequestForm

from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView


class LeaveCreateView(GroupRequiredMixin, CreateView):
    """
    View to create leave requests of a loggedin employee
    """
    model = LeaveRequest
    form_class = LeaveRequestForm
    template_name = 'leave/leave_request_form.html'
    success_url = reverse_lazy("leave:leave-request-list")


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"request":self.request})
        return kwargs

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        
        self.object = form.save(commit = False)
        self.object.employee = self.request.user
        self.object.save()

        return super().form_valid(form)
