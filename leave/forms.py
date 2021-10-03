from leave.models.leave_request import LeaveRequest
from leave.models.employee_leave import EmployeeLeave

from django import forms
from django.db.models import Q


class LeaveRequestForm(forms.ModelForm):

    class Meta:
        model = LeaveRequest
        exclude = ['employee','approval_status']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        self.user = self.request.user
        super(LeaveRequestForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field in ("date_from","date_to"):
                self.fields[field].widget.attrs.update({'placeholder': 'YYYY-MM-DD'})

    def clean(self):
        cleaned_data = super().clean()
        leave = cleaned_data.get('leave')
        to_date = cleaned_data.get("date_to")
        from_date = cleaned_data.get("date_from")

        if to_date < from_date:
            raise forms.ValidationError("Date to must be greater than Date from.")

        # if particular leave request already exists raise error message
        leave_request_exists = LeaveRequest.objects.filter(
            Q(date_from__lte = to_date) & Q(date_to__gte = to_date) |
            Q(date_from__lte = from_date) & Q(date_to__gte = from_date),
            employee = self.user,
            ).exists()
        if leave_request_exists:
            raise forms.ValidationError(
                "Leave request for date %(d1)s to %(d2)s already exists.",
                code = "request_exists",
                params = {'d1':from_date, 'd2':to_date}
                )

        # if no leave days remaining or if requested leave days exceeds the remaining days raise error
        remaining_days = EmployeeLeave.objects.filter(
			employee = self.user,
			leave = leave,
            ).first().remaining_leave

        requested_days = LeaveRequest.no_of_days(from_date, to_date)
        if (requested_days > remaining_days)|(remaining_days == 0):
            raise forms.ValidationError(
				"Leave request exceeds remaining number of leaves ",
                )