from django.db import models

# Create your models here.
class Supplier(models.Model):
    title           = models.CharField(max_length=100)
    description     = models.TextField()
    is_active       = models.BooleanField(default=True)
    created_at      = models.DateTimeField(auto_now_add=True)
