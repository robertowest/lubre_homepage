from django.contrib import admin

from . import models

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = models.Profile
    list_display = model.list_display
    list_display_links = model.list_display_links
    search_fields = model.search_fields
