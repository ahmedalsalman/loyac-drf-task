# Generated by Django 3.1 on 2020-08-09 02:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loyac_api', '0010_auto_20200809_0506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='application_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 9, 5, 21, 53, 991067)),
        ),
        migrations.AlterField(
            model_name='program',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 9, 5, 21, 53, 990068)),
        ),
    ]
