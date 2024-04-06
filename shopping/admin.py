from django.contrib import admin
from .models import Add_To_Cart, Orders


@admin.register(Add_To_Cart)
class Add_To_CartAdmin(admin.ModelAdmin):
    list_display = ['potential_buyer', 'items_in_cart']
    ordering = ['potential_buyer']
    list_per_page = 20


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'order_products', 'order_summ', 'order_time', 'buyer_name']
    ordering = ['order_time']
    search_fields = ['order_id']
    list_per_page = 20

