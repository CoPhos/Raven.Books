from rest_framework import serializers
from .models import Book, BookImage, Authors, Tags, Publisher
from versatileimagefield.serializers import VersatileImageFieldSerializer

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ('first_name','last_name','profile_photo','about_author',)

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('publisher_name',)

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('tag_name',)

class BookDetailSerializer(serializers.ModelSerializer):
    publisher =  serializers.SlugRelatedField(read_only=True, slug_field="publisher_name")
    tag = serializers.SlugRelatedField(read_only=True,many=True, slug_field="tag_name")
    author = AuthorSerializer(many=True)
    class Meta:
        fields = ('author','title','isbn','publication_year', 'sold_count','edition','price','quant_in_stock','publisher','language','tag','description','pages','weight',)
        model = Book

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True)
    class Meta:
        fields = ('id','title', 'price', 'author','publication_year')
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
        model = BookImage
        fields = ('image',)

class BookImage_BookSerializer(serializers.ModelSerializer):
    images = BookImageSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id' ,'images','title')