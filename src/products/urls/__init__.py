from django.urls import include, path

app_name = "products"

urlpatterns = [
    path("supplier/", include("products.urls.supplier", namespace="supplier_products_api")),
    path("organization/", include("products.urls.organization", namespace="organization_products_api")),
    path("public/", include("products.urls.public", namespace="public_products_api")),
]
