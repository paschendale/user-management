from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add any custom fields here
    date_of_birth = models.DateField(null=True, blank=True)
    pass