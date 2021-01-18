from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, related_name="%(class)s_created"
    )
    updated_by = models.ForeignKey(
        "user.User", on_delete=models.SET_NULL, related_name="%(class)s_updated", null=True
    )

    class Meta:
        abstract = True
        app_label = "base"
