from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    calc_count = models.IntegerField(default=0, verbose_name='calculation')
