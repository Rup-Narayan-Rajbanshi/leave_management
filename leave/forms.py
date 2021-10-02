from django import forms
from leave.models.leave_request import LeaveRequest
from leave.models.employee_leave import EmployeeLeave

from django.db.models import Q

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        exclude = ['employee','approval_status']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        self.user = self.request.user
        return super(LeaveRequestForm, self).__init__(*args, **kwargs)

    def clean_date_to(self):
        from_date = self.cleaned_data.get('date_from')
        to_date = self.cleaned_data.get('date_to')

        if to_date < from_date:
            raise forms.ValidationError(
        "Date to must be greater than Date from."
        )
        return to_date

    def clean(self):
        cleaned_data = super().clean()

        leave = cleaned_data.get('leave')
        to_date = cleaned_data.get("date_to")
        from_date = cleaned_data.get("date_from")

        request = LeaveRequest.objects.filter(
            Q(date_from__lte = to_date) & Q(date_to__gte = to_date) |
            Q(date_from__lte = from_date) & Q(date_to__gte = from_date),
            employee = self.user,
        )

        if request.exists():
            raise forms.ValidationError(
                "Leave request for date %(d1)s to %(d2)s already exists.",
                code = "request_exists",
                params = {'d1':from_date, 'd2':to_date}
            )

        remaining_days = EmployeeLeave.objects.filter(
			employee = self.user,
			leave = leave,
		).first().remaining_leave

        requested_days = LeaveRequest.no_of_days(from_date, to_date)
        if (requested_days > remaining_days) or (remaining_days==0):
            raise forms.ValidationError(
				"Leave request exceeds remaining number of leaves ",
			)