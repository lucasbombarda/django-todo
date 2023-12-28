from django.db import models


# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=255)
    details = models.TextField(null=True, blank=True, default=None)
    completed = models.BooleanField(default=False)

    finished_at = models.DateTimeField(null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Task #{self.id}"
