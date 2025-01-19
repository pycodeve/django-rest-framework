from django.db import models

# Create your models here.
class Category(models.Model):
    title       = models.CharField(max_length=100)
    is_active   = models.BooleanField(default=True)

class Product(models.Model):
    title           = models.CharField(max_length=100)
    description     = models.TextField()
    price           = models.DecimalField(max_digits=6, decimal_places=2)
    is_active       = models.BooleanField(default=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    category        = models.ForeignKey(
        Category,  
        related_name="categories", 
        on_delete=models.CASCADE,
        default=None
    )