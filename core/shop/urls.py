from django.urls import path
from .views import ProductDetailView, ProductListView

urlpatterns = [
    path('product/', ProductDetailView.as_view(), name='product-detail'),
    path('products/', ProductListView.as_view(), name='products-list'),
]