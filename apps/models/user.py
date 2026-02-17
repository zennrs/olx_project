


from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.managers import CustomUserManager


class User(AbstractUser):

    class Status(models.TextChoices):
        WORKER = "worker", "Ishchi"
        EMPLOYER = "employer", "Ish beruvchi"
        SELLER = "seller", "Sotuvchi"
        SIMPLE = "simple", "Oddiy"

    username = None

    email = models.EmailField(unique=True)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.SIMPLE
    )

    image = models.ImageField(
        upload_to="users/",
        blank=True,
        null=True
    )
    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
