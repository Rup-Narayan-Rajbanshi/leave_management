from django.urls import path
from leave.views.leave_request_view import LeaveCreateView
from leave.views.leave_request_list import LeaveRequestListView
from leave.views.monthly_leave_list import MonthlyLeaveListView

app_name = 'leave'

urlpatterns = [
    path('add_leave/', LeaveCreateView.as_view(), name='add-leave'),
    path('leave_request_list/',LeaveRequestListView.as_view(), name='leave-request-list'),
    path('monthly_leave_list/<uuid:employee_id>/',MonthlyLeaveListView.as_view(), name='monthly-leave-list'),
]