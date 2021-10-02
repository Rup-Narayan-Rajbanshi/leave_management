from django.db import models
from helpers.models import BaseModel
from employee.models import CustomUser
from .leave import Leave


class EmployeeLeave(BaseModel):
    employee = models.ForeignKey(CustomUser, null = True, on_delete = models.CASCADE, related_name="leaves")
    leave = models.ForeignKey(Leave, null=True, on_delete=models.CASCADE, related_name="leaves")
    total_days = models.FloatField(null=True, blank=True)
    remaining_leave = models.FloatField(null=True, blank=True)
    can_apply_leave = models.BooleanField(default=True)

    def __str__(self):
        return self.employee.first_name

    class Meta:
        ordering = ['-created_at']
