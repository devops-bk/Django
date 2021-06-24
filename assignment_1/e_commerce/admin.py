from django.contrib import admin

# Register your models here.
from .models import User, Product, Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']

admin.site.register(User)

admin.site.register(Product, ProductAdmin)

admin.site.register(Order)
