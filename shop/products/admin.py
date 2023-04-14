from django.contrib import admin
from .models import ProductCategory, Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price", "quantity")
    list_display_links = ("id", "name")


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)
