from django.urls import path

from products.views import RawMaterialListCreateAPIView

app_name = "supplier_product"

urlpatterns = [
    path(
        "",
        RawMaterialListCreateAPIView.as_view(),
        name="v1-supplier-create-raw-material",
    ),
]
