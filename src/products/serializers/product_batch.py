from rest_framework import serializers

from products.models import ProductBatch


class ProductBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBatch
        fields = "__all__"
