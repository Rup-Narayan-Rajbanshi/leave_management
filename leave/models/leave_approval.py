from django.db import models
from helpers.models import BaseModel
from .leave_request import LeaveRequest
from helpers.constants import APPROVAL_TYPE
from helpers.choices import APPROVAL_CHOICES


class LeaveApproval(BaseModel):	
    leave_request = models.ForeignKey(LeaveRequest, on_delete=models.PROTECT, null=True, related_name="leave_approval")
    approval_status = models.CharField(choices=APPROVAL_CHOICES, max_length=15, default=APPROVAL_TYPE['PENDING'])

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.leave_request.employee.first_name

    def save(self, *args, **kwargs):
        ''' On approve leave request update remaining leaves '''
        if self.approval_status==APPROVAL_TYPE['YES']:
            self.leave_request.update(approval_status=APPROVAL_TYPE['YES'])
        elif self.approval_status==APPROVAL_TYPE['NO']:
            self.leave_request.update(approval_status=APPROVAL_TYPE['NO'])
        return super(LeaveApproval, self).save(*args, **kwargs)
