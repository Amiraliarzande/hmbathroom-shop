from django.views.generic import TemplateView
from django.db.models import Prefetch

from shop.models import Category, Product, ProductImage


class HomeView(TemplateView):
    template_name = "index/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = Category.objects.filter(
            is_active=True
        ).order_by(
            "sort_order", "name"
        ).prefetch_related(
            Prefetch(
                "products",
                queryset=Product.objects.filter(
                    is_active=True
                ).prefetch_related(
                    Prefetch(
                        "images",
                        queryset=ProductImage.objects.order_by(
                            "sort_order", "-id"
                        ),
                    )
                ).order_by("-created_at", "-id"),
                to_attr="active_products",
            )
        )

        for category in categories:
            category.latest_product = next(
                (
                    product
                    for product in category.active_products
                    if product.images.all()
                ),
                None,
            )

        popular_products = Product.objects.filter(
            is_active=True,
            category__is_active=True,
        ).select_related(
            "category"
        ).prefetch_related(
            "images"
        ).order_by(
            "sort_order", "name"
        )[:8]

        context["categories"] = categories
        context["popular_products"] = popular_products

        return context