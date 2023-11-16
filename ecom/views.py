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


@require_GET
@token_required
def get_products(request):
    try:
        products = inventory.get_products()
        return products
    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})


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
def add_product(request):
    try:
        data = json.loads(request.body)
        product_name = data.get("product_name")
        price = data.get("price")
        quantity = data.get("quantity")
        expiry_date = data.get("expiry_date")
        manufacturer = data.get("manufacturer")
        supplier_info = data.get("supplier_info")
        category = data.get("category")

        prod = inventory.add_product(
            product_name,
            price,
            quantity,
            expiry_date,
            manufacturer,
            supplier_info,
            category,
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
        product_name = data.get("product_name")
        price = data.get("price")
        quantity = data.get("quantity")
        expiry_date = data.get("expiry_date")
        supplier_info = data.get("supplier_info")
        description = data.get("description")
        category = data.get("category")

        update = inventory.update_product(
            product_uid,
            product_name,
            price=price,
            quantity=quantity,
            expiry=expiry_date,
            supplier_info=supplier_info,
            description=description,
            category=category,
        )

        return update
    except Exception as e:
        logger.warning(str(e))
        return JsonResponse({"success": False, "info": "Kindly try again --p2prx2--"})
