from rest_framework import serializers
from books.serializers import BookSerializer
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    """Serializes author instances"""

    books = serializers.SerializerMethodField()

    def get_books(self, obj):
        books_queryset = obj.books
        return BookSerializer(books_queryset, many=True).data

    class Meta:
        model = Author
        fields = ('id', 'name', 'date_of_birth', 'gender', 'books', 'created_at')
        # extra_kwargs is used to set extra settings for the Meta fields
        extra_kwargs = {'created_at': {'read_only': True}}
