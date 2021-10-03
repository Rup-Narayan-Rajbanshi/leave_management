from django.contrib.auth import (authenticate ,get_user_model ,login, logout)
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from employee.models import CustomUser
from leave.models.employee_leave import EmployeeLeave

from django.db.models import Count, Sum
from django.contrib.auth.decorators import user_passes_test


# Create your views here.
def login_view(request):
	"""
	Login View
	"""
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		login(request, user)
		return HttpResponseRedirect(reverse('home'))
	context = {'form': form}
	return render(request, 'employee/login.html', context=context)

def logout_view(request):
	"""
	Logout view
	"""
	logout(request)
	return HttpResponseRedirect(reverse('employee:login'))

@user_passes_test(lambda u: u.is_superuser)
def employee_list(request):
	"""
	List of employees with remaining leaves, total leaves taken
	"""
	employees = CustomUser.objects.filter(groups__name='employee').annotate(
																		remaining_leave_count=Sum('leaves__remaining_leave'),
																		total_leave_count=Sum('leaves__total_days'))
	context = {
		'employees': employees,
	}
	return render(request, 'employee/list.html', context=context)
