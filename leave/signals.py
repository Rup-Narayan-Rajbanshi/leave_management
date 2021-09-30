from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Leave, EmployeeLeave
from employee.models import CustomUser


@receiver(post_save, sender = Leave)
def create_employee_leave(sender, instance, created, *args, **kwargs):
  if created:
    leave = instance
    employees = CustomUser.objects.filter(groups__name__iexact = "employee")
    for employee in employees:
        employee_leave= EmployeeLeave.objects.get_or_create(employee=employee, leave=leave)