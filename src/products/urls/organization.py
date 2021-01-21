from django.urls import path

from products.views import RawMaterialListCreateAPIView

app_name = "organization_raw_material"

urlpatterns = [
    path(
        "",
        RawMaterialListCreateAPIView.as_view(),
        name="v1-organization-create-raw-material",
    ),
]
