# Generated by Django 2.2.13 on 2020-08-26 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.IntegerField(default=1, verbose_name='是否活跃'),
        ),
    ]
