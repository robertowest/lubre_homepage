from django.contrib import admin

from . import models

admin.site.register(models.Pais)
admin.site.register(models.Provincia)
admin.site.register(models.Departamento)
admin.site.register(models.Localidad)

# class ProvinciaFilter(admin.SimpleListFilter):
#     title = 'Provincia'
#     parameter_name = 'parent'

#     def lookups(self, request, model_admin):
#         array = []
#         queryset = models.georef.objects.filter(nivel='02')
#         for element in queryset:
#             if element.active == True:
#                 array.append([element.id, element.nombre])
#         return array

#     def default_value(self):
#         return models.georef.objects.filter(nivel='02').filter(nombre='Tucuman')[0].nombre

#     def queryset(self, request, queryset):
#         if self.value():
#             return queryset.filter(parent=int(self.value()))


# class NivelFilter(admin.SimpleListFilter):
#     title = "Nivel"
#     parameter_name = 'nivel'

#     def lookups(self, request, model_admin):
#         return (
#             ('03', 'Departamento'),
#             ('04', 'Municipio'),
#             ('05', 'Localidad'),
#         )

#     def default_value(self):
#         return '02'

#     def queryset(self, request, queryset):
#         if self.value():
#             return queryset.filter(nivel=self.value())


# @admin.register(models.georef)
# class GeoRefAdmin(admin.ModelAdmin):
#     model = models.georef
#     list_display = model.list_display
#     list_display_links = model.list_display_links
#     search_fields = model.search_fields
#     # list_filter = model.list_filter
#     list_filter = [ProvinciaFilter, NivelFilter]


admin.site.register(models.Domicilio)
admin.site.register(models.Diccionario)
admin.site.register(models.Comunicacion)


# registra todos los modelos
# se debería ejecutar al final de todo, por si ya existe alguna definición

# from django.apps import apps
# models = apps.get_models()
# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass
