from rest_framework import serializers
from .models import Capsule

class CapsuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capsule
        fields = ["id", "title", "message", "release_date", "is_public", "author", "created_at"]
        read_only_fields = ["id", "author", "created_at"]

    def to_representation(self, instance):
        """Ocultar mensaje si la cápsula aún no está disponible"""
        rep = super().to_representation(instance)
        if not instance.is_available():
            rep["message"] = "⏳ Esta cápsula aún no está disponible."
        return rep