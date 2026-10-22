from django.contrib import admin
from order.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'price', 'quantity')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'user', 'status', 'total_price', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('order_number', 'user__email')
    readonly_fields = ('order_number', 'total_price', 'created_at', 'updated_at')
    inlines = [OrderItemInline]