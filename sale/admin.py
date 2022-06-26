# Imports:
# 3rd party:
from django.contrib import admin

# Internal:
from .models import Sale


class SaleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'percentage',
        'start_date',
        'end_date',
    )

    ordering = ('start_date',)



# Register your models here.
admin.site.register(Sale, SaleAdmin)
