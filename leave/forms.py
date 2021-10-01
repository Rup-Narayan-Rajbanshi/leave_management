from django import forms
from leave.models.leave import LeaveRequest

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        exclude = ['approval_status']
    
    # def clean(self):
    #     '''
    #     Verify both passwords match.
    #     '''
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get("password")
    #     password_2 = cleaned_data.get("password_2")
    #     if password is not None and password != password_2:
    #         self.add_error("password_2", "Your passwords must match")
    #     return cleaned_data

