# Generated by Django 3.2.6 on 2021-08-26 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20210826_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='sold_count',
            field=models.IntegerField(default=0),
        ),
    ]
