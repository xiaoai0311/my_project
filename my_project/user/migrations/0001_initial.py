# Generated by Django 2.2.13 on 2020-08-26 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='用户名')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('course', models.CharField(max_length=20, verbose_name='课程')),
                ('session', models.CharField(max_length=20, verbose_name='角色')),
                ('is_active', models.BooleanField(default=True, verbose_name='角色活跃情况')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
