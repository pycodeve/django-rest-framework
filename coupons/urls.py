from django.urls import path

from coupons.views import list_coupons, detail_coupon

urlpatterns = [
    path('coupons/', list_coupons),
    path('coupons/<int:pk>/', detail_coupon),
]
