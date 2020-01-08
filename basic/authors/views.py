from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from .models import Author

# Local
from .serializers import AuthorSerializer


class AuthorView(ModelViewSet):
    """Handle creating and updating author"""
    serializer_class = AuthorSerializer
    queryset = Author.objects.all().prefetch_related('books')
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
