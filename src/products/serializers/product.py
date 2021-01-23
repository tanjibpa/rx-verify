from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        
    def create(self, validated_data):
        print(validated_data)
        return super(ProductSerializer, self).create(validated_data)

