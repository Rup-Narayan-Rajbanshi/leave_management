from django.urls import path
from leave.views.leave_request_view import LeaveCreateView
from leave.views.leave_request_list import LeaveRequestListView

app_name = 'leave'

urlpatterns = [
    path('add_leave/', LeaveCreateView.as_view(), name='add-leave'),
    path('list/',LeaveRequestListView.as_view(), name='list'),
]