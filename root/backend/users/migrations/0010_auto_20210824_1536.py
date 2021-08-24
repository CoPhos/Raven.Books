# Generated by Django 3.2.6 on 2021-08-24 20:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_customuser_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='image_ppoi_customuser',
            new_name='customuser_ppoi',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 24, 20, 36, 24, 943747, tzinfo=utc)),
        ),
    ]
