from django.db import models
from django.utils import timezone
import uuid
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = 'Employee'

    def __str__(self):
        return self.first_name +" "+self.last_name

    # @property
    # def full_name(self):
    #     return self.first_name + " "+ self.last_name