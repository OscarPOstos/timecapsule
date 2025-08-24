from django.urls import path
from .views import CapsuleListCreateView, CapsuleDetailView, CapsuleOpenView, CapsuleSubscribeView, CapsuleSubscribersView, ActiveCapsulesStatsView, TopCapsulesStatsView

urlpatterns = [
    path('capsules/', CapsuleListCreateView.as_view(), name="capsule-list-create"),
    path('capsules/<int:pk>/', CapsuleDetailView.as_view(), name="capsule-detail"),
    path('capsules/<int:id>/open/', CapsuleOpenView.as_view(), name="capsule-open"),
    path('capsules/<int:id>/subscribe/', CapsuleSubscribeView.as_view(), name="capsule-subscribe"),
    path('capsules/<int:id>/subscribers/', CapsuleSubscribersView.as_view(), name="capsule-subscribers"),
    path("stats/active/", ActiveCapsulesStatsView.as_view(), name="stats-active"),
    path("stats/top/", TopCapsulesStatsView.as_view(), name="stats-top"),
]