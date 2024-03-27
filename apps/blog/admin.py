from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin):
    """
    Админ-панель модели категорий
    """
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post)
