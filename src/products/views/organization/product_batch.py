from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from products.models import Product, ProductBatch
from products.serializers import ProductSerializer, ProductBatchSerializer
from user.serializers import UserSerializerLite


class ProductBatchListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ProductBatch.objects.all()
    serializer_class = ProductBatchSerializer

    def perform_create(self, serializer):
        serializer.save(
            created_by=UserSerializerLite(self.request.user).data,
            updated_by=UserSerializerLite(self.request.user).data,
        )
