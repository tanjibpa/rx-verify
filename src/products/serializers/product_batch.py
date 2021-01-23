from rest_framework import serializers

from products.models import ProductBatch


class ProductBatchSerializer(serializers.ModelSerializer):
    product_details = serializers.SerializerMethodField(required=False)

    class Meta:
        model = ProductBatch
        fields = "__all__"

    def get_product_details(self, obj: ProductBatch):
        raw_materials = [
            {"id": raw_material.id, "name": raw_material.name}
            for raw_material in obj.product.raw_materials.all()
        ]
        return {"name": obj.product.name, "raw_materials": raw_materials}
