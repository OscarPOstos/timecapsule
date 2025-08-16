from rest_framework import generics, permissions
from .models import Capsule
from .serializers import CapsuleSerializer

class CapsuleListCreateView(generics.ListCreateAPIView):
    queryset = Capsule.objects.filter(is_public=True)
    serializer_class = CapsuleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CapsuleDetailView(generics.RetrieveDestroyAPIView):
    queryset = Capsule.objects.all()
    serializer_class = CapsuleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("Solo el autor puede eliminar esta cápsula.")
        instance.delete()