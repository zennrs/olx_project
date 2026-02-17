from django.contrib import admin

from apps.models import User, Announcement
from apps.models.categorys import Category
from apps.models.announcement import AnnouncementImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


class ProductImageStackedInline(admin.StackedInline):
    model = AnnouncementImage
    min_num = 1
    extra = 0
