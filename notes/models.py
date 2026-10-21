from django.db import models

# Create your models here.
class Notes(models.Model):
    class Priority(models.TextChoices):
        LOW = 'low', "Low"
        MEDIUM = 'medium', 'Medium'
        HIGH = 'high', 'High'

    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=100, default='', blank=True)
    priority = models.CharField(max_length=15, choices=Priority.choices, default=Priority.MEDIUM)
    is_pinned = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title