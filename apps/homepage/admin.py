from django.contrib import admin

# Register your models here.
from . import models


class EntriesAdmin(admin.ModelAdmin):
    list_display = ['section', 'label', 'ordered', 'active']
    ordering = ['section', 'ordered']

    list_filter = ['section', 'active']
    search_fields = ['label']
    list_per_page = 20

admin.site.register(models.Entries, EntriesAdmin)

admin.site.register(models.Category)
admin.site.register(models.Tag)

class PostAdmin(admin.ModelAdmin):
    list_display = models.Post.list_display
    search_fields = models.Post.search_fields
    list_filter = models.Post.list_filter
admin.site.register(models.Post, PostAdmin)




admin.site.register(models.Grupo);
admin.site.register(models.Producto);
