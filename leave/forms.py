from django import forms
from leave.models.leave_request import LeaveRequest
from leave.models.employee_leave import EmployeeLeave

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        exclude = ['employee','approval_status']
    
    # def clean(self):
    #     '''
       
    #     '''
    #     cleaned_data = super().clean()
    #     date_from = cleaned_data.get("date_from")
    #     date_to = cleaned_data.get("date_to")
    #     leave_type = cleaned_data.get("leave_type")
    #     no_of_days = LeaveRequest.no_of_days(date_from, date_to, leave_type)
    #     employee_leave = EmployeeLeave.objects.get()

        
    #     if password is not None and password != password_2:
    #         self.add_error("password_2", "Your passwords must match")
    #     return cleaned_data

