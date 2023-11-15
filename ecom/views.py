from django.shortcuts import render
from CRMS.decorators import check_fields, token_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from ecom.utils import Inventory
from django.http import JsonResponse
import json
import logging

logger = logging.getLogger(__name__)
# Create your views here.

inventory = Inventory()


@csrf_exempt
@require_POST
@token_required
@check_fields(
    [
        "product_name",
        "price",
        "quantity",
        "expiry_date",
        "manufacturer",
        "supplier_info",
    ]
)
def create_products(request):
    try:
        data = json.loads(request.body)
        product_name = data.get("product_name")
        price = data.get("price")
        quantity = data.get("quantity")
        expiry_date = data.get("expiry_date")
        manufacturer = data.get("manufacturer")
        supplier_info = data.get("supplier_info")

        prod = inventory.add_product(
            product_name, price, quantity, expiry_date, manufacturer, supplier_info
        )
        return prod

    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})


@csrf_exempt
@require_POST
def update_product(request):
    try:
        data = json.loads(request.body)
        product_uid = data.get("product_uid")
        price = data.get("price")
        quantity = data.get("quantity")
        expiry_date = data.get("expiry_date")

        update = inventory.update_product(
            product_uid,
            price=price,
            quantity=quantity,
            expiry_date=expiry_date,
        )

        return update
    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})
