from django.contrib import admin
from .models import (
    Product, OrderItem, Order, ColorVariation,
    SizeVariation, Address
)

class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'address_line_1',
        'address_line_2',
        'zip_code',
        'city',
        'country',
        'address_type',
    ]

admin.site.register(Address, AddressAdmin)
admin.site.register(ColorVariation)
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(SizeVariation)
