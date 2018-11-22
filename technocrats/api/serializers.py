# api/serializers.py

from rest_framework import serializers
from .models import Bucketlist


class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""

    owner = serializers.ReadOnlyField(source='owner.username') # ADD THIS LINE

    class Meta:
        """Map this serializer to a model and their fields."""
        model = Bucketlist
        fields = ('id', 'name', 'owner_id', 'date_created', 'date_modified') # ADD 'owner_id'
        read_only_fields = ('date_created', 'date_modified')