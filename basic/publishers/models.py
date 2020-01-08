from django.db import models
from django.contrib.auth.models import BaseUserManager


class Publisher(models.Model):
    """
    Schema for publisher instances.
    """
    name = models.TextField(null=False)
    created_at = models.DateField(editable=False, auto_now=True)
    objects = BaseUserManager()

    def __str__(self):
        """Return string representation of our publisher"""
        return self.name
