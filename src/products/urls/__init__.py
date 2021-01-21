from django.urls import include, path

from products.urls.supplier import *

app_name = "products"

urlpatterns = [
    path("supplier/", include("products.urls.supplier", namespace="supplier_products_api")),
    path("organization/", include("products.urls.organization", namespace="organization_products_api")),
]
