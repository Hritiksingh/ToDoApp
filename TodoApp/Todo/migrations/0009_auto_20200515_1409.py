# Generated by Django 3.0.5 on 2020-05-15 14:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0008_auto_20200515_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyworks',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 5, 15, 14, 9, 8, 186484)),
        ),
    ]
