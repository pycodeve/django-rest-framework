from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import ProductSerializer
from .models import Product
from .permissions import IsCustomer

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsCustomer]

    @action(['post'], detail=True, url_path='set-on-status')
    def set_on_status(self, request, pk=None):
        product = self.get_object()
        product.is_active = True
        product.save()
        return Response({'status': "Product is active"})
    
    @action(['post'], detail=True, url_path='set-off-status')
    def set_off_status(self, request, pk=None):
        product = self.get_object()
        product.is_active = False
        product.save()
        return Response({'status': "Product is inactive"})