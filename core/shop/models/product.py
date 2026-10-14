from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["sort_order", "name"]


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products"
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    model_number = models.CharField(max_length=100, blank=True, null=True)
    short_description = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["sort_order", "name"]


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(upload_to="products/")
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - Image"

    class Meta:
        ordering = ["sort_order", "id"]


class ProductSpecification(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name="specification"
    )
    size = models.CharField(max_length=100, blank=True, null=True)
    pan = models.CharField(max_length=100, blank=True, null=True)
    flush = models.CharField(max_length=100, blank=True, null=True)
    seat = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} - Specifications"

    class Meta:
        verbose_name = "Product Specification"
        verbose_name_plural = "Product Specifications"


class ProductOption(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="options"
    )
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} - {self.key}"

    class Meta:
        verbose_name = "Product Option"
        verbose_name_plural = "Product Options"