from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.JSONField(default=dict)
    updated_by = models.JSONField(default=dict)

    class Meta:
        abstract = True
        app_label = "base"
