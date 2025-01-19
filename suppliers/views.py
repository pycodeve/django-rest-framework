from .serializers import SupplierSerializer
from .models import Supplier

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# GET /api/suppliers/ => list
# POST /api/suppliers/ => create
class ListSuppliersView(APIView):

    allowed_methods = ['GET', 'POST']
    
    def get(self, request):
        coupons = Supplier.objects.all()
        serializer = SupplierSerializer(coupons, many=True)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = SupplierSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
# GET /api/suppliers/<pk>/ => retrieve
# PUT /api/suppliers/<pk>/ => update
# DELETE /api/suppliers/<pk>/ => delete
class DetailSuppliersView(APIView):

    allowed_methods = ['GET', 'PUT', 'DELETE']

    def get(self, request, pk):
        try:
            coupon = Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SupplierSerializer(coupon)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            coupon = Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SupplierSerializer(coupon, data=request.data)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        try:
            coupon = Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        coupon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)