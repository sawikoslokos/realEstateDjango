# Generated by Django 3.2.8 on 2021-10-21 07:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='contactDate',
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]