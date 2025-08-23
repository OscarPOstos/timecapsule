from rest_framework import serializers
from .models import Capsule, CapsuleSubscription

class CapsuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capsule
        fields = ["id", "title", "release_date", "is_public", "created_by", "created_at"]
        read_only_fields = ["created_by", "created_at"]


class CapsuleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capsule
        fields = ["id", "title", "message", "release_date", "is_public", "created_by", "created_at"]
        read_only_fields = ["created_by", "created_at"]


class CapsuleSubscriptionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = CapsuleSubscription
        fields = ["id", "user", "subscribed_at"]