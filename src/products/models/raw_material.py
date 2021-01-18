from django.db import models

from base.models import BaseModel


class RawMaterial(BaseModel):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "raw_materials"
        verbose_name_plural = "Raw Materials"
        verbose_name = "Raw Material"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.name
