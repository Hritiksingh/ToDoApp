# Generated by Django 3.0.5 on 2020-05-13 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0004_auto_20200513_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyworks',
            name='date',
            field=models.DateTimeField(blank=True),
        ),
    ]
