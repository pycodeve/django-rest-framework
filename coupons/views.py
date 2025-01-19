from .serializers import CouponSerializer
from .models import Coupon

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# GET /api/coupons/ => list
# POST /api/coupons/ => create
@api_view(['GET', 'POST'])
def list_coupons(request):

    if request.method == 'GET':
        coupons = Coupon.objects.all()
        serializer = CouponSerializer(coupons, many=True)

        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CouponSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
# GET /api/coupons/<pk>/ => retrieve
# PUT /api/coupons/<pk>/ => update
# DELETE /api/coupons/<pk>/ => delete
@api_view(['GET', 'PUT', 'DELETE'])
def detail_coupon(request, pk):

    try:
        coupon = Coupon.objects.get(pk=pk)
    except Coupon.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CouponSerializer(coupon)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = CouponSerializer(coupon, data=request.data)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'DELETE':
        coupon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)