# Generated by Django 2.1 on 2018-10-08 09:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0005_auto_20181008_0603'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_page',
            name='updated_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]