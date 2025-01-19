from django.urls import path

from suppliers.views import ListSuppliersView, DetailSuppliersView

urlpatterns = [
    path('suppliers/', ListSuppliersView.as_view()),
    path('suppliers/<int:pk>/', DetailSuppliersView.as_view()),
]