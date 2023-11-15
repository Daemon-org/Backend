from django.http import JsonResponse
import arrow
from ecom.models import Product
from django.http import JsonResponse
import arrow
from ecom.models import Product
from django.db import transaction
import logging

logger = logging.getLogger(__name__)


class Inventory:
    def add_product(
        self, product_name, price, quantity, expiry_date, manufacturer, supplier_info
    ):
        try:
            if Product.objects.filter(name=product_name).exists():
                return JsonResponse({"error": "Product already exists"}, status=409)

            # Create a new product object
            product = Product.objects.create(
                name=product_name,
                price=price,
                quantity=quantity,
                expiry_date=expiry_date,
                manufacturer=manufacturer,
                supplier_info=supplier_info,
                added_on=arrow.now().datetime,
            )

            if product:
                return JsonResponse(
                    {"success": "Product added successfully"}, status=200
                )
            else:
                return JsonResponse({"error": "Failed to add product"}, status=500)

        except Exception as e:
            logger.warning(str(e))
            return JsonResponse(
                {"success": False, "info": "Kindly try again --p2prx2--"}
            )

    @transaction.atomic()
    def update_product(self, product_uid, price,expiry,quantity):
        try:
            product = Product.objects.get(id=product_uid)
            product.price = price
            product.quantity = quantity
            product.expiry_date = expiry 
            product.save(update_fields=["price","quantity","expiry_date"])
            return JsonResponse({"success": "Product updated successfully"}, status=200)
        except Exception as e:
            logger.warning(str(e))
            return JsonResponse(
                {"success": False, "info": "Kindly try again --p2prx2--"}
            )
