# TODO:add a celery task for checking expired products and notifying the admin through email and cache it


from celery import shared_task
from ecom.utils import Inventory
from CRMS.notif import Notify
from ecom.models import Product

inventory = Inventory()
notify = Notify()


@shared_task
def check_expiry():
    products = Product.objects.values_list("product_uid", flat=True)
    results = []

    for product_uid in products:
        exp = inventory.check_expiry(product_uid)
        results.append(exp)

    return results
