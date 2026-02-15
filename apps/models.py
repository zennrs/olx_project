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


class Product(Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # favorites =
    view_count = models.IntegerField(default=0)
