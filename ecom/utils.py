from django.http import JsonResponse
import arrow
from ecom.models import Product
from django.http import JsonResponse
import arrow
from ecom.models import Product
from django.db import transaction
from django.shortcuts import get_object_or_404

from CRMS.notif import Notify

import logging

logger = logging.getLogger(__name__)

notify = Notify()
class Inventory:
    def get_products(self):
        try:
            products = Product.objects.values(
                "product_uid",
                "product_name",
                "price",
                "quantity",
                "description",
                "category",
                "expiry_date",
                "manufacturer",
                "supplier_info",
            ).all()
            if products:
                return JsonResponse({"success": True, "data": list(products)})
            else:
                return JsonResponse({"success": False, "info": "No products found"})
        except Exception as e:
            logger.warning(str(e))
            return JsonResponse(
                {"success": False, "info": "Kindly try again --p2prx2--"}
            )

    def add_product(
        self,
        product_name,
        price,
        quantity,
        expiry_date,
        manufacturer,
        supplier_info,
        category,
        description,
    ):
        try:
            if Product.objects.filter(product_name=product_name).exists():
                return JsonResponse({"error": "Product already exists"}, status=409)

            # Create a new product object
            product = Product.objects.create(
                product_name=product_name,
                price=price,
                quantity=quantity,
                expiry_date=expiry_date,
                manufacturer=manufacturer,
                supplier_info=supplier_info,
                category=category,
                description=description,
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
    def update_product(
        self,
        product_uid,
        product_name=None,
        price=None,
        expiry=None,
        quantity=None,
        supplier_info=None,
        description=None,
        category=None,
    ):
        try:
            product = Product.objects.get(product_uid=product_uid)

            if product_name is not None:
                product.product_name = product_name
            if price is not None:
                product.price = price
            if expiry is not None:
                product.expiry_date = expiry
            if quantity is not None:
                product.quantity = quantity
            if supplier_info is not None:
                product.supplier_info = supplier_info
            if description is not None:
                product.description = description
            if category is not None:
                product.category = category

            product.save()

            return JsonResponse({"success": "Product updated successfully"}, status=200)
        except Exception as e:
            logger.warning(str(e))
            return JsonResponse(
                {"success": False, "info": " Unable to u[pdate product"}, status=500
            )

    def delete_product(self, product_uid):
        try:
            product = Product.objects.get(product_uid=product_uid)
            product.delete()
            return JsonResponse({"success": "Product deleted successfully"}, status=200)
        except Exception as e:
            logger.warning(str(e))
            return JsonResponse(
                {"success": False, "info": "Unable to delete product"}, status=500
            )

    def search_product(self, query):
        try:
            products = Product.objects.values(
                "product_uid",
                "product_name",
                "price",
                "quantity",
                "description",
                "category",
                "expiry_date",
                "manufacturer",
                "supplier_info",
                "added_on",
            ).filter(product_name__icontains=query)
            if products:
                return JsonResponse({"success": True, "data": list(products)})
            else:
                return JsonResponse({"success": False, "info": "No products found"})
        except Exception as e:
            logger.warning(str(e))
            return JsonResponse(
                {"success": False, "info": "Kindly try again --p2prx2--"}
            )

    def filter_products(self, category=None, manufacturer=None):
        try:
            filter_params = {}
            if category:
                filter_params["category"] = category
            if manufacturer:
                filter_params["manufacturer"] = manufacturer

            products = Product.objects.values(
                "product_uid",
                "product_name",
                "price",
                "quantity",
                "description",
                "category",
                "expiry_date",
                "manufacturer",
                "supplier_info",
                "added_on",
            ).filter(**filter_params)

            if products:
                return JsonResponse({"success": True, "data": list(products)})
            else:
                return JsonResponse({"success": False, "info": "No products found"})

        except Exception as e:
            logger.warning(str(e))
            return JsonResponse(
                {"success": False, "info": "Kindly try again --p2prx2--"}
            )


# TODO: update the code to send a list of expired product_names via mail and same with expired ones
    def check_expiry(self, product_uid):
        try:
            product = get_object_or_404(Product, product_uid=product_uid)
            exp_prod = {"product_name": product.product_name}
            current_time = arrow.utcnow()
            recipient = "khemikal2016@gmail.com"
            context1 = {
                "email": recipient,
                "template": "expired",
                "context": {"email": recipient, "product_name": exp_prod["product_name"]},
            }
            context2 = {
                "email": recipient,
                "template": "expiring-soon",
                "context": {"email": recipient, "product_name": exp_prod["product_name"]},
            }
            if product.expiry_date < current_time:
                notify.send_sms_or_email(medium="email", recipient=recipient, context=context1)
                return JsonResponse({"status": "Expired"})

            if product.expiry_date <= current_time.shift(months=6):
                notify.send_sms_or_email(medium="email", recipient=recipient, context=context2)
                return JsonResponse({"status": "Expiring soon"})
            else:
                return JsonResponse({"status": "Not expired"})

        except Exception as e:
            logger.warning(str(e))
            return JsonResponse({"status": "Error"})

