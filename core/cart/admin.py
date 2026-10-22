from django.contrib import admin
from cart.models import Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    raw_id_fields = ('product',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'session_key', 'get_total_items', 'get_total_price', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__email', 'session_key')
    inlines = [CartItemInline]