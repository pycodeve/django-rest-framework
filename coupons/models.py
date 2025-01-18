from django.db import models

# Create your models here.
class Coupon(models.Model):
    title           = models.CharField(max_length=100)
    is_active       = models.BooleanField(default=True)
    finished_at     = models.DateTimeField()
    created_at      = models.DateTimeField(auto_now_add=True)
