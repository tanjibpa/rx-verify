import uuid
from django.db import models

from base.models import BaseModel


class ProductBatch(BaseModel):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    batch_number = models.UUIDField(default=uuid.uuid4, editable=False)
    mfg_date = models.DateField()
    expiration_date = models.DateField()

    class Meta:
        db_table = "product_batches"
        verbose_name_plural = "Product Batches"
        verbose_name = "Product Batch"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.batch_number
