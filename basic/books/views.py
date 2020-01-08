from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from .models import Book, BookGenre

# Local
from .serializers import BookSerializer, BookGenreSerializer


class BookView(ModelViewSet):
    """Handle creating and updating author"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ('name',)


class BookGenreView(ModelViewSet):
    """Handle creating and updating author"""
    serializer_class = BookGenreSerializer
    queryset = BookGenre.objects.all().prefetch_related('books')
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
