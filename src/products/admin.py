from django.contrib import admin

from .models import RawMaterial, Product, ProductBatch


class RawMaterialAdmin(admin.ModelAdmin):
    fields = ("name",)


class ProductAdmin(admin.ModelAdmin):
    fields = ("name", "raw_materials")


class ProductBatchAdmin(admin.ModelAdmin):
    fields = ("product", "mfg_date", "expiration_date")


admin.site.register(RawMaterial, RawMaterialAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductBatch, ProductBatchAdmin)
