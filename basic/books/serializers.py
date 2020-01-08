from rest_framework import serializers
from .models import Book, BookGenre


class BookSerializer(serializers.ModelSerializer):
    """Serializes book instances"""

    class Meta:
        model = Book
        fields = ('id', 'name', 'genre', 'authors', 'publisher', 'created_at',)
        # extra_kwargs is used to set extra settings for the Meta fields
        extra_kwargs = {'created_at': {'read_only': True}}


class BookGenreSerializer(serializers.ModelSerializer):
    """Serializes book instances"""

    class Meta:
        model = BookGenre
        fields = ('id', 'genre', 'description',)
