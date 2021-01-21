from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny

from products.models import ProductBatch
from products.serializers import ProductBatchSerializer


class ProductRetrieveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = ProductBatch.objects.all()
    serializer_class = ProductBatchSerializer
    lookup_field = "batch_number"
