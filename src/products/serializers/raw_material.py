from rest_framework import serializers

from products.models import RawMaterial


class RawMaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterial
        fields = "__all__"
