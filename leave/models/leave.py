from django.db import models
from helpers.models import BaseModel


class Leave(BaseModel):
    name = models.CharField(max_length=50)
    no_of_days = models.FloatField()
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name