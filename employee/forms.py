from django import forms
from django.contrib.auth import authenticate

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields:
			if field in ("username"):
				self.fields[field].widget.attrs.update({'placeholder': 'Username'})
			if field in ("password"):
				self.fields[field].widget.attrs.update({'placeholder': 'Password'})
			self.fields[field].label=''

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		user = authenticate(username=username, password=password)

		if not user:
			raise forms.ValidationError('The user doesnot exist')
		if not user.check_password(password):
			raise forms.ValidationError('The password is incorrect')
		if not user.is_active:
			raise forms.ValidationError('The user is not active')
















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