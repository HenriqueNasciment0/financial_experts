from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_company = models.BooleanField(default=False)
    is_expert = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
