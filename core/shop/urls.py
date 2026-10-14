from django.urls import path

from .views import product


app_name = "shop"

urlpatterns = [
    path(
        "products/",
        product.ProductListView.as_view(),
        name="product_list",
    ),
    path(
        "products/<slug:slug>/",
        product.ProductDetailView.as_view(),
        name="product_detail",
    ),
]