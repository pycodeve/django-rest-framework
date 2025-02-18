from django.urls import path
from products.views import ListCategoriesView, DetailCategoriesView
from rest_framework.routers import DefaultRouter
from .viewsets import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('categories/', ListCategoriesView.as_view()),
    path('categories/<int:pk>/', DetailCategoriesView.as_view()),
] + router.urls