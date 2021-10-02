from django.views.generic import DetailView
from leave.models.leave_request import LeaveRequest
from employee.models import CustomUser
from leave.forms import LeaveRequestForm
from helpers.constants import APPROVAL_TYPE
from leave.utils import filter_leave_dates

from django.urls import reverse_lazy, reverse
from datetime import date, timedelta


class MonthlyLeaveListView(DetailView):
    template_name = 'leave/monthly_leave_list.html'

    def get_object(self, queryset=None):
        return CustomUser.objects.get(id=self.kwargs.get("employee_id"))

    def get_queryset(self):
        employee = self.get_object()
        year = date.today().year
        leaves_in_year = LeaveRequest.objects.filter(employee=employee, approval_status=APPROVAL_TYPE['YES'], date_from__year=year)
        return leaves_in_year

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        leaves_in_year = self.get_queryset()

        leaves_dates = []
        for leave in leaves_in_year:
            date_from = leave.date_from
            date_to = leave.date_to
            delta = date_to - date_from
            for i in range(delta.days + 1):
                day = date_from + timedelta(days=i)
                leaves_dates.append(day)

        leaves_dates = sorted(leaves_dates)
        leaves_dates_dict = dict()
        for month in range(1,13):
            date_list = []
            for date in leaves_dates:
                if month == date.month:
                    date_list.append(date)
                    leaves_dates_dict[month]=len(date_list)
        
        print(leaves_dates_dict)

        context = {
            'monthly_leaves': leaves_dates_dict
        }
        return context