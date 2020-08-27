from django.db import models

# Create your models here.
from user.models import User

class Attendence(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    sign_time = models.DateTimeField('签到时间', auto_now_add=True)
    is_onTime = models.CharField('到课情况', max_length=12,default='')

    class Meta:
        db_table='attendence'


