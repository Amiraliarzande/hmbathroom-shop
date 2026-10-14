from django.views.generic import ListView, DetailView
from django.db.models import Prefetch

from ..models import Category, Product


class ProductListView(ListView):
    model = Product
    template_name = "shop/products.html"
    context_object_name = "products"

    def get_queryset(self):
        return (
            Product.objects.filter(
                is_active=True,
                category__is_active=True,
            )
            .select_related("category")
            .prefetch_related("images", "options")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["categories"] = (
            Category.objects.filter(is_active=True)
            .prefetch_related(
                Prefetch(
                    "products",
                    queryset=Product.objects.filter(is_active=True),
                    to_attr="active_products",
                )
            )
        )

        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "shop/product.html"
    context_object_name = "product"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return (
            Product.objects.filter(
                is_active=True,
                category__is_active=True,
            )
            .select_related("category", "specification")
            .prefetch_related("images", "options")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["related_products"] = (
            Product.objects.filter(
                category=self.object.category,
                category__is_active=True,
                is_active=True,
            )
            .exclude(pk=self.object.pk)
            .select_related("category")
            .prefetch_related("images")
            .order_by("sort_order", "name")[:4]
        )

        return context