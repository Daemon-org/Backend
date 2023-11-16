from django.contrib import admin
from ecom.models import Product, Purchase, History

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = tuple(field.name for field in Product._meta.fields)


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = tuple(field.name for field in Purchase._meta.fields)


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = tuple(field.name for field in History._meta.fields)
