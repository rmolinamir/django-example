from django.db import models
from django.contrib.auth.models import BaseUserManager

TYPE_MALE, TYPE_FEMALE, TYPE_NEUTRAL = range(0, 3)
GENDER_TYPE = (
    (TYPE_MALE, 'Male'),
    (TYPE_FEMALE, 'Female'),
    (TYPE_NEUTRAL, 'Neutral'),
)


class Author(models.Model):
    """
    Schema for author instances.
    """
    name = models.TextField(null=False)
    date_of_birth = models.DateField(null=False)
    gender = models.SmallIntegerField(
        choices=GENDER_TYPE,
        default=TYPE_NEUTRAL,
    )
    created_at = models.DateField(editable=False, auto_now=True)
    objects = BaseUserManager()

    def __str__(self):
        """Return string representation of our author"""
        return self.name
