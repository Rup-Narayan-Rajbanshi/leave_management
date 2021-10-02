from django.db import models
from helpers.choices import APPROVAL_CHOICES, LEAVE_CHOICES
from helpers.constants import APPROVAL_TYPE, LEAVE_TYPE
from helpers.models import BaseModel
from employee.models import CustomUser
from leave.models.leave import Leave
from leave.models.employee_leave import EmployeeLeave
from leave.utils import no_of_days


class LeaveRequest(BaseModel):	
    employee = models.ForeignKey(CustomUser, on_delete=models.PROTECT, null=True, related_name="leave_requests")
    leave = models.ForeignKey(Leave, on_delete=models.PROTECT, null=True, related_name="leave_requests")
    date_from = models.DateField()
    date_to = models.DateField()
    remarks = models.TextField()
    approval_status = models.CharField(choices=APPROVAL_CHOICES, max_length=15, default=APPROVAL_TYPE['PENDING'])

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.employee.first_name

    @staticmethod
    def no_of_days(date_from, date_to):
        return no_of_days(date_to, date_from)
       

    def save(self, *args, **kwargs):
        '''
        On approve leave request update remaining leaves
        '''
        number_of_days = self.__class__.no_of_days(self.date_from, self.date_to)
        if self.approval_status == APPROVAL_TYPE['YES']:
            employee_leave = EmployeeLeave.objects.get(employee=self.employee, leave=self.leave)
            employee_leave.remaining_leave =  employee_leave.remaining_leave - number_of_days
            employee_leave.save()
        return super(LeaveRequest, self).save(*args, **kwargs)
