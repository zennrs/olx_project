from django.contrib.auth.models import AbstractUser
from django.db import models

from django.db.models import Model


class Category(Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    image = models.ImageField(upload_to="category/", null=True, blank=True)

    def product_count(self):
        # total =
        pass


    def __str__(self):
        return self.name


