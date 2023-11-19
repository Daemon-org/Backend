# TODO:add a celery task for checking expired products and notifying the admin through email and cache it


from celery import shared_task
from ecom.utils import Inventory
from CRMS.notif import Notify


inventory = Inventory()
notify = Notify()
