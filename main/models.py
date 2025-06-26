from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Calculations(models.Model):
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL,
                             related_name='user', verbose_name='user')
    img = models.ImageField(upload_to='photos/%Y/%m/%d', default=None, blank=True, null=True,
                            verbose_name='image')
    result = models.CharField(max_length=40, verbose_name='emotion')

