# Imports:
# 3rd party:
from django.contrib import admin

# Internal:
from .models import Product, Genre


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'subtitle',
        'authors',
        'price',
        'rating',
        'image',
    )

    ordering = ('authors',)

class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Genre, GenreAdmin)