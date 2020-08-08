# Generated by Django 3.1 on 2020-08-08 13:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loyac_api', '0006_auto_20200808_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='applicant',
        ),
        migrations.AlterField(
            model_name='program',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 8, 16, 46, 0, 352033)),
        ),
        migrations.AlterField(
            model_name='program',
            name='supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supervising', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Apllication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('application_date', models.DateTimeField(default=datetime.datetime(2020, 8, 8, 16, 46, 0, 354031))),
                ('applicant', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='loyac_api.program')),
            ],
        ),
    ]