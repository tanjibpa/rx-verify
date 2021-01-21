from django.urls import include, path

from products.urls.organization import *

app_name = "products"

urlpatterns = [
    path("products/", include("products.urls.organization", namespace="organization_products_api")),
]
