from django.db import models

from base.models import BaseModel
from .raw_material import RawMaterial
from .product import Product


class Order(BaseModel):
    raw_materials = models.ManyToManyField(RawMaterial)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    approved = models.BooleanField(default=False)

    class Meta:
        db_table = "orders"
        verbose_name_plural = "Orders"
        verbose_name = "Order"
        ordering = ["-updated_at"]
