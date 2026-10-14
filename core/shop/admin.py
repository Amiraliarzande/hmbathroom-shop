from django.contrib import admin
from .models.product import (
    Category,
    Product,
    ProductImage,
    ProductSpecification,
    ProductOption,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_active", "sort_order")
    list_filter = ("is_active",)
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("sort_order", "name")


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductOptionInline(admin.TabularInline):
    model = ProductOption
    extra = 1


class ProductSpecificationInline(admin.StackedInline):
    model = ProductSpecification
    extra = 0
    max_num = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "model_number",
        "category",
        "price",
        "is_active",
        "sort_order",
    )
    list_filter = ("category", "is_active")
    search_fields = ("name", "model_number", "description")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("sort_order", "name")

    inlines = [
        ProductImageInline,
        ProductSpecificationInline,
        ProductOptionInline,
    ]


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("product", "alt_text", "sort_order")
    list_filter = ("product__category",)
    search_fields = ("product__name", "alt_text")
    ordering = ("product", "sort_order")


@admin.register(ProductSpecification)
class ProductSpecificationAdmin(admin.ModelAdmin):
    list_display = ("product", "size", "pan", "flush", "seat")
    search_fields = ("product__name",)


@admin.register(ProductOption)
class ProductOptionAdmin(admin.ModelAdmin):
    list_display = ("product", "key", "value")
    search_fields = ("product__name", "key", "value")