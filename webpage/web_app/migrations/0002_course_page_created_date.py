# Generated by Django 2.1 on 2018-10-08 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_page',
            name='created_date',
            field=models.DateField(auto_now=True),
        ),
    ]