from django.views.generic.edit import CreateView
from leave.models.leave_request import LeaveRequest
from leave.forms import LeaveRequestForm

from django.urls import reverse_lazy, reverse


class LeaveCreateView(CreateView):
    model = LeaveRequest
    form_class = LeaveRequestForm
    template_name = 'leave/leave_request_form.html'
    success_url = reverse_lazy("leave:leave-request-list")

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        
        self.object = form.save(commit = False)
        self.object.employee = self.request.user
        self.object.save()

        return super().form_valid(form)
