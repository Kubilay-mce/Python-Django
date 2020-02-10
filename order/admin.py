from django.contrib import admin
from order.models import Order, OrderDetail, ShopCart
# Register your models here.

class ShopCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'order', 'price', 'quantity', 'total', 'create_at')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'surname', 'address', 'phone', 'city', 'total', 'note', 'status')



admin.site.register(ShopCart,ShopCartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)















