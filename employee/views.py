from django.contrib.auth import (authenticate ,get_user_model ,login, logout)
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse, Http404
from .views import UserLoginForm
from employee.models import CustomUser
from leave.models.employee_leave import EmployeeLeave

from django.db.models import Count, Sum


# Create your views here.
def login_view(request):
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
	logout(request)
	return HttpResponseRedirect(reverse('user:login'))

def employee_list(request):
	employees = CustomUser.objects.filter(groups__name='employee').annotate(
																		remaining_leave_count=Sum('leaves__remaining_leave'),
																		total_leave_count=Sum('leaves__total_days'))
	context = {
		'employees': employees,
	}
	return render(request, 'employee/list.html', context=context)
