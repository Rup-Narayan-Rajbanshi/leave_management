from django.urls import path
from employee.views import login_view, logout_view, employee_list

app_name = 'employee'

urlpatterns = [
    path('login/', login_view, name='login'),
    # path('logout/', logout_view, name='logout'),
    path('employees/', employee_list, name='employees-list'),

]