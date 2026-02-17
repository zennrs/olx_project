from django.contrib.auth.models import AbstractUser
from django.db import models

from django.db.models import Model
from mptt.models import MPTTModel


class Category(MPTTModel):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")


    class MPTTMeta:
        order_insertion_by = ["name"]

    image = models.ImageField(upload_to="category/", null=True, blank=True)


    def __str__(self):
        return self.name


