from django.urls import path

from products.views import ProductListCreateAPIView, ProductBatchListCreateAPIView

app_name = "organization_raw_material"

urlpatterns = [
    path(
        "", ProductListCreateAPIView.as_view(), name="v1-organization-create-product",
    ),
    path(
        "product-batch",
        ProductBatchListCreateAPIView.as_view(),
        name="v1-organization-create-product-batch",
    ),
]
