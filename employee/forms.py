from django import forms
from .models import CustomUser

class EmployeeForm(forms.ModelForm):
    password = forms.CharField(max_length=64, required=False, widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = '__all__'