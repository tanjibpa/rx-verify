from django.urls import path

from products.views import ProductRetrieveAPIView

app_name = "public_product"

urlpatterns = [
    path(
        "<str:batch_number>",
        ProductRetrieveAPIView.as_view(),
        name="v1-supplier-get-product-batch",
    ),
]
