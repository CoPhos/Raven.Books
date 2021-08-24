from rest_framework import serializers
from .models import Book, BookImage
from versatileimagefield.serializers import VersatileImageFieldSerializer

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title',)
        model = Book

class BookImageSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(
         sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
            ('medium_square_crop', 'crop__400x400'),
            ('small_square_crop', 'crop__50x50')
        ]
    )
    class Meta:
        fields = ('image',)
        model = BookImage