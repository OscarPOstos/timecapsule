from django.urls import path
from .views import CapsuleListCreateView, CapsuleDetailView

urlpatterns = [
    path('capsules/', CapsuleListCreateView.as_view(), name="capsule-list-create"),
    path('capsules/<int:pk>/', CapsuleDetailView.as_view(), name="capsule-detail"),
]