from django.urls import path

from products.views import ListCategoriesView, DetailCategoriesView

urlpatterns = [
    path('categories/', ListCategoriesView.as_view()),
    path('categories/<int:pk>/', DetailCategoriesView.as_view()),
]