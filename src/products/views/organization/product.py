from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from products.models import Product
from products.serializers import ProductSerializer
from user.serializers import UserSerializerLite


class ProductListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(
            created_by=UserSerializerLite(self.request.user).data,
            updated_by=UserSerializerLite(self.request.user).data,
        )
