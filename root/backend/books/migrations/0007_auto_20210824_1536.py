# Generated by Django 3.2.6 on 2021-08-24 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20210824_1533'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authors',
            old_name='image_ppoi_author',
            new_name='author_ppoi',
        ),
        migrations.RenameField(
            model_name='bookimage',
            old_name='image_ppoi_bookimage',
            new_name='bookImage_ppoi',
        ),
    ]
