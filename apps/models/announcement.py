from django.db import models

from django.db.models import Model, DateTimeField, TextField, CharField, ForeignKey, ImageField

from apps.models import User
from root import settings


class Announcement(Model):

    class Status(models.TextChoices):
       Active = 'active', 'Active'
       Expected = 'expected', 'Expected'
       Unpaid = 'unpaid', 'Unpaid'
       Unactive = 'unactive', 'Unactive'



    class AnnouncementType(models.TextChoices):
        SIMPLE = "simple", "Oddiy"
        VIP = "vip", "VIP"

    name = CharField(max_length=255)
    description = TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    view_count = models.PositiveIntegerField(default=0)
    owner = ForeignKey(User, related_name="announcements", on_delete=models.CASCADE)

    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name="products")

    favorites = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="favorite_products",
        blank=True
    )

    status = CharField(max_length=20, choices=Status.choices, default=Status.Expected)
    product_type = CharField(max_length=10, choices=AnnouncementType.choices, default=AnnouncementType.SIMPLE)
    user= ForeignKey(User, related_name="user_products", on_delete=models.CASCADE)
    location = CharField(max_length=255, null=True, blank=True)  # Location_filed





    def save(self, *args, **kwargs):
        self.name = self.name.strip()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name



class AnnouncementImage(models.Model):
    product = ForeignKey(Announcement, on_delete=models.CASCADE)
    image = ImageField(upload_to="product/%Y/%m")
