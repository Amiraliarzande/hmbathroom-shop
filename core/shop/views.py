from django.views.generic import TemplateView

class ProductDetailView(TemplateView):
    template_name = 'shop/product.html'

class ProductListView(TemplateView):
    template_name = 'shop/products.html'