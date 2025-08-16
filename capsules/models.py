from django.db import models
from django.contrib.auth.models import User

class Capsule(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    release_date = models.DateTimeField()  # Fecha en la que se podrá abrir
    is_public = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="capsules")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def is_available(self):
        """Verifica si la cápsula ya puede ser abierta."""
        from django.utils import timezone
        return timezone.now() >= self.release_date