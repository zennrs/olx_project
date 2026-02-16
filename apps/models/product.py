from django.db import models

from django.db.models import Model

from root import settings


class Product(models.Model):

    class Status(models.TextChoices):
        NEW = "new", "Yangi"
        DONT_USE = "dont_use", "Ishlatilmagan"
        OLD = "old", "Eski"

    class ProductType(models.TextChoices):
        SIMPLE = "simple", "Oddiy"
        VIP = "vip", "VIP"

    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    view_count = models.PositiveIntegerField(default=0)

    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name="products")

    favorites = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="favorite_products",
        blank=True
    )

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)

    product_type = models.CharField(max_length=10, choices=ProductType.choices, default=ProductType.SIMPLE)

    def save(self, *args, **kwargs):
        self.name = self.name.strip()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
