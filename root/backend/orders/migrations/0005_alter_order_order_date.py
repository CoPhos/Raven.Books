# Generated by Django 3.2.6 on 2021-08-24 20:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_order_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 24, 20, 21, 42, 875736, tzinfo=utc)),
        ),
    ]
