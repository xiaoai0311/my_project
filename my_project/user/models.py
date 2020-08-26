from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField('用户名',max_length=20)
    password = models.CharField('密码',max_length=32)
    course = models.CharField('课程',max_length=20)
    session = models.CharField('角色',max_length=20)
    is_active = models.BooleanField('角色活跃情况',default=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'user'