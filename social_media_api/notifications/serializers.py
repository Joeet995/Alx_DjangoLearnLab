from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['actor', 'verb', 'target', 'timestamp', 'is_read']
        read_only_fields = ['is_read']