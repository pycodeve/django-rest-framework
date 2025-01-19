from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price can't be negative")
        return value
    
    def validate(self, attrs):
        if len(attrs["title"]) < 5 or len(attrs["description"]) < 5:
            raise serializers.ValidationError("Title and descriptions must be at least 5 characters long")

        return super().validate(attrs)
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
