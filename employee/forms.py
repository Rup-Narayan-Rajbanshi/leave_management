# from django import forms
# from .models import CustomUser

# class EmployeeForm(forms.ModelForm):
#     # password = forms.CharField(widget=forms.PasswordInput)
#     # password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

#     class Meta:
#         model = CustomUser
#         fields = '__all__'
    
#     # def clean(self):
#     #     '''
#     #     Verify both passwords match.
#     #     '''
#     #     cleaned_data = super().clean()
#     #     password = cleaned_data.get("password")
#     #     password_2 = cleaned_data.get("password_2")
#     #     if password is not None and password != password_2:
#     #         self.add_error("password_2", "Your passwords must match")
#         # return cleaned_data

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         if commit:
#             user.save()
#         return user