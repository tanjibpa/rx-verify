from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from products.models import RawMaterial
from products.serializers import RawMaterialsSerializer


class RawMaterialListCreateAPIView(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialsSerializer
