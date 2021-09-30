from django.db import models
from django.utils import timezone
import uuid


class BaseModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def force_filter(self, **kwargs):
        return super().get_queryset().filter(**kwargs)


class BaseModel(models.Model):
    """
    Base model for possibly every other model.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)

    objects = BaseModelManager()

    def update(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        self.save()
        return self

    # all the common queryset filters goes here
    @classmethod
    def queryset(cls, **kwargs):
        return cls.objects.filter(**kwargs)

    @classmethod
    def force_filter(cls, **kwargs):
        return cls.objects.filter(**kwargs)

    @classmethod
    def new(cls, **kwargs):
        return cls.objects.create(**kwargs)

    @classmethod
    def flush(cls, force_delete=False, **kwargs):
        return cls.objects.filter(**kwargs).delete()

    def delete(self, force_delete=False, **kwargs):
        super(BaseModel, self).delete(**kwargs)

    class Meta:
        abstract = True