from django.urls import path
from ecom.views import *

urlpatterns = [
    path("products/", get_products),
    path("add_product/", add_product),
    path("update_product/", update_product),
    path("delete_product/", delete_product),
    path("search_product/", search_product),
    path("filter_products/", filter_products),
    path("expired_products/", fetch_expired_products),
    path("almost_expired_products/", fetch_almost_expired_products),
    path("register_purchase/", register_purchase),
    path("total_purchases/", fetch_purchases),
    path("generate_report/", generate_report),
    path("fetch_lowstock/", get_lowstock),
    path("analytics/", get_analytics),
]
