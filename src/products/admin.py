from django.contrib import admin
from django.contrib.auth.models import Group

from .models import RawMaterial, Product, ProductBatch, Order


class RawMaterialAdmin(admin.ModelAdmin):
    fields = ("name",)


class ProductAdmin(admin.ModelAdmin):
    fields = ("name", "raw_materials")


class ProductBatchAdmin(admin.ModelAdmin):
    fields = ("product", "mfg_date", "expiration_date", "approved")


class OrderAdmin(admin.ModelAdmin):
    fields = ["raw_materials", "product", "quantity"]

    def change_view(self, request, object_id, form_url='', extra_context=None):
        g = Group.objects.get(name='Supplier')
        if g in request.user.groups.all() and "approved" not in self.fields:
            self.fields.append("approved")
        return super().change_view(
            request, object_id, form_url, extra_context=extra_context,
        )


admin.site.register(RawMaterial, RawMaterialAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductBatch, ProductBatchAdmin)
admin.site.register(Order, OrderAdmin)
