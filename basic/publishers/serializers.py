from rest_framework import serializers
from .models import Publisher


class PublisherSerializer(serializers.ModelSerializer):
    """Serializes publisher instances"""

    class Meta:
        model = Publisher
        fields = ('id', 'name', 'books', 'created_at')
        # extra_kwargs is used to set extra settings for the Meta fields
        extra_kwargs = {'created_at': {'read_only': True}}
