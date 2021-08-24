from django.contrib import admin
from .models import Book, Publisher, Authors, BookImage, Tags
# Register your models here.
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Authors)
admin.site.register(BookImage)
admin.site.register(Tags)