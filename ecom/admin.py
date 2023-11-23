from django.contrib import admin
from ecom.models import Product, Purchase, History

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = tuple(field.name for field in Product._meta.fields)
    search_fields = ["product_name", "description","manufacturer"]


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = tuple(field.name for field in Purchase._meta.fields)
    search_fields = [
        "product__product_name",
        "product__description",
    ]


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = tuple(field.name for field in History._meta.fields)
    search_fields = [
        "purchase__product__product_name",
        "purchase__product__description",
    ]
