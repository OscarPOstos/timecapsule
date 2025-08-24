from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from .models import Capsule, CapsuleSubscription
from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import CapsuleSerializer, CapsuleDetailSerializer, CapsuleSubscriptionSerializer
from django.utils.timezone import now
from django.db.models import Count

class CapsuleListCreateView(generics.ListCreateAPIView):
    queryset = Capsule.objects.filter(is_public=True)
    serializer_class = CapsuleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class CapsuleDetailView(generics.RetrieveDestroyAPIView):
    queryset = Capsule.objects.all()
    serializer_class = CapsuleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("Solo el autor puede eliminar esta cápsula.")
        instance.delete()

class CapsuleOpenView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id):
        capsule = get_object_or_404(Capsule, id=id)

        if capsule.release_date > timezone.now():
            return Response({"error": "Esta cápsula aún no está disponible"}, status=status.HTTP_403_FORBIDDEN)

        serializer = CapsuleDetailSerializer(capsule)
        return Response(serializer.data)


class CapsuleSubscribeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id):
        capsule = get_object_or_404(Capsule, id=id)
        subscription, created = CapsuleSubscription.objects.get_or_create(capsule=capsule, user=request.user)

        if not created:
            return Response({"message": "Ya estabas suscrito a esta cápsula"}, status=status.HTTP_200_OK)

        return Response({"message": "Te has suscrito a la cápsula"}, status=status.HTTP_201_CREATED)


class CapsuleSubscribersView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id):
        capsule = get_object_or_404(Capsule, id=id)
        subscribers = capsule.subscriptions.all()
        serializer = CapsuleSubscriptionSerializer(subscribers, many=True)
        return Response(serializer.data)

# 📈 Publicaciones activas del día
class ActiveCapsulesStatsView(APIView):
    def get(self, request):
        today = now().date()
        active_capsules = Capsule.objects.filter(created_at__date=today).count()
        return Response({"date": str(today), "active_capsules": active_capsules})


# 📈 Pensamientos más populares
class TopCapsulesStatsView(APIView):
    def get(self, request):
        top_capsules = (
            Capsule.objects.annotate(num_subs=Count("subscriptions"))
            .order_by("-num_subs")[:5]
        )
        serializer = CapsuleSerializer(top_capsules, many=True)
        return Response(serializer.data)