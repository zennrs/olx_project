from django.contrib import admin

from apps.models.category import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
