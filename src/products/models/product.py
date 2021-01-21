from django.db import models

from base.models import BaseModel
from .raw_material import RawMaterial


class Product(BaseModel):
    name = models.CharField(max_length=100)
    raw_materials = models.ManyToManyField(RawMaterial)

    class Meta:
        db_table = "products"
        verbose_name_plural = "Products"
        verbose_name = "Product"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.name
