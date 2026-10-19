from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=100, unique = True)
    phone = models.CharField(max_length=20, unique=True)
    company = models.CharField(max_length=100, blank = True, default="")
    notes = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name