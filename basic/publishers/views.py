from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from .models import Publisher

# Local
from .serializers import PublisherSerializer


class PublisherView(ModelViewSet):
    """Handle creating and updating publisher"""
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all().prefetch_related('books')
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
