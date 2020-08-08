# Generated by Django 3.1 on 2020-08-08 12:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loyac_api', '0003_auto_20200808_1432'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='program',
            options={'verbose_name_plural': 'Program'},
        ),
        migrations.AddField(
            model_name='program',
            name='applicant',
            field=models.ManyToManyField(blank=True, related_name='programs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='program',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 8, 15, 29, 44, 258924)),
        ),
        migrations.AddField(
            model_name='program',
            name='supervisor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='supervising', to='loyac_api.customuser'),
            preserve_default=False,
        ),
    ]