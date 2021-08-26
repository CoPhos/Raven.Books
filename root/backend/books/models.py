from django.db import models
from django.contrib.auth.models import User

from versatileimagefield.fields import VersatileImageField, PPOIField
# Create your models here.

class Publisher(models.Model):
    publisher_name = models.CharField(max_length=50, null=False, blank=False,)

    def __str__(self):
        return self.publisher_name

class Authors(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    profile_photo = VersatileImageField(
        'Image',
        upload_to='images/',
        ppoi_field='author_ppoi'
    )
    author_ppoi = PPOIField()
    about_author = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.first_name

class Tags(models.Model):
    tag_name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.tag_name

class Book(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    isbn = models.CharField(max_length=17, null=False, blank=False)
    publication_year = models.DateTimeField()
    edition = models.CharField(max_length=2, null=False, blank=False)
    price = models.DecimalField(max_digits=4, decimal_places=2,null=False, blank=False)
    quant_in_stock = models.BigIntegerField()
    language = models.CharField(max_length=2, null=False, blank=False)
    weight = models.CharField(max_length=4, null=False, blank=False)
    pages = models.CharField(max_length=4, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    sold_count = models.IntegerField(blank=False, null=False, default=0)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name="book_publisher")
    tag = models.ManyToManyField('Tags', related_name="book_tag")
    author = models.ManyToManyField('Authors', related_name="book_author")

    def __str__(self):
        return self.title

class BookImage(models.Model):
    image = VersatileImageField(
        'Image',
        upload_to='images/',
        ppoi_field='bookImage_ppoi'
    )
    bookImage_ppoi = PPOIField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="images")