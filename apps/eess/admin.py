from django.contrib import admin

from . import models


@admin.register(models.Cartilla)
class CartillaAdmin(admin.ModelAdmin):
    model = models.Cartilla
    list_display = model.list_display
    list_display_links = model.list_display_links
    search_fields = model.search_fields
    list_filter = model.list_filter
    ordering = ['id']
