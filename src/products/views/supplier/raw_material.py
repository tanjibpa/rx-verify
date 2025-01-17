from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.request import Request

from products.models import RawMaterial
from products.serializers import RawMaterialsSerializer
from user.serializers import UserSerializerLite


class RawMaterialListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialsSerializer

    def perform_create(self, serializer):
        serializer.save(
            created_by=UserSerializerLite(self.request.user).data,
            updated_by=UserSerializerLite(self.request.user).data,
        )
