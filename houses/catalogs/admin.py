from django.contrib import admin

from .models import Catalog


class CatalogAdmin(admin.ModelAdmin):
    list_display = (
        'photo',
        'description',
        'price',
    )


admin.site.register(Catalog)
