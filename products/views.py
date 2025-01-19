from .serializers import CategorySerializer
from .models import Category

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

class ListCategoriesView(ListAPIView, CreateAPIView):
    """
    List all categories or create a new category.
    """
    allowed_methods = ['GET', 'POST']
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
class DetailCategoriesView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a category instance.
    """
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = CategorySerializer
    queryset = Category.objects.all()