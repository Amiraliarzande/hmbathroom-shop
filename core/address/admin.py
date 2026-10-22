from django.contrib import admin
from address.models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'label', 'full_name', 'city', 'postcode', 'country', 'is_default', 'created_at')
    list_filter = ('is_default', 'country', 'created_at')
    search_fields = ('user__email', 'label', 'full_name', 'city', 'postcode', 'phone')
    list_editable = ('is_default',)
    ordering = ('-is_default', '-created_at')