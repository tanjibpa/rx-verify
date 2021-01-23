from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from products.models import ProductBatch
from products.serializers import ProductBatchSerializer


class ProductRetrieveAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = ProductBatch.objects.all()
    serializer_class = ProductBatchSerializer
    lookup_field = "batch_number"

    def get(self, request, *args, **kwargs):
        batch = self.get_object()
        if not batch.approved:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        return super(ProductRetrieveAPIView, self).get(request, args, kwargs)
