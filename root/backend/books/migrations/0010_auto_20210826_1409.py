# Generated by Django 3.2.6 on 2021-08-26 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_alter_bookimage_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.RemoveField(
            model_name='book',
            name='tags',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='book_author', to='books.Authors'),
        ),
        migrations.AddField(
            model_name='book',
            name='tag',
            field=models.ManyToManyField(related_name='book_tag', to='books.Tags'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_publisher', to='books.publisher'),
        ),
    ]
