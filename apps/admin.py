from django.contrib import admin

from apps.models import User, Product
from apps.models.category import Category
from apps.models.product import ProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


class ProductImageStackedInline(admin.StackedInline):
    model = ProductImage
    min_num = 1
    extra = 0
