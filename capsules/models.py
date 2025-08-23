from django.db import models
from django.contrib.auth.models import User

class Capsule(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    release_date = models.DateTimeField()
    is_public = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="capsules")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CapsuleSubscription(models.Model):
    capsule = models.ForeignKey(Capsule, on_delete=models.CASCADE, related_name="subscriptions")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscriptions")
    subscribed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("capsule", "user")

    def __str__(self):
        return f"{self.user.username} -> {self.capsule.title}"