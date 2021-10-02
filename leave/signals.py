from django.dispatch import receiver
from django.db.models.signals import post_save
from leave.models.leave import Leave
from leave.models.employee_leave import EmployeeLeave
from leave.models.leave_request import LeaveRequest
from employee.models import CustomUser


@receiver(post_save, sender = Leave)
def create_employee_leave(sender, instance, created, *args, **kwargs):
    """
    Allocate a employee_leave on creating any new leave.
    """
    if created:
        leave = instance
        employees = CustomUser.objects.filter(groups__name__iexact = "employee")
        for employee in employees:
            employee_leave= EmployeeLeave.objects.get_or_create(employee=employee,
                                                                leave=leave,
                                                                total_days=leave.no_of_days,
                                                                remaining_leave=leave.no_of_days)


@receiver(post_save, sender = CustomUser)
def create_employee_leave(sender, instance, created, *args, **kwargs):
    """
    Allocate a employee_leave on creating any new leave.
    """
    if created:
        employee = instance
        leaves = Leave.objects.all()
        if leaves:
            for leave in leaves:
                employee_leave= EmployeeLeave.objects.get_or_create(employee=employee,
                                                                    leave=leave,
                                                                    total_days=leave.no_of_days,
                                                                    remaining_leave=leave.no_of_days)

