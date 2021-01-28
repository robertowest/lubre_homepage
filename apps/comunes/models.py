from smart_selects.db_fields import ChainedForeignKey

from django.db import models
from django.urls import reverse
from datetime import datetime

from django_currentuser.middleware import get_current_user

# como campo de un modelo (ForeignKey)
# from django_currentuser.db.models import CurrentUserField
# class CommonStruct(models.Model):
#    created_by = CurrentUserField()

class CommonStruct(models.Model):
    active = models.BooleanField('Activo', default=True, null=False, blank=False)
    created = models.DateTimeField('Creado', auto_now_add=True, editable=False, null=True, blank=True)
    created_by = models.CharField('Creado por', max_length=15, editable=False, null=True, blank=True)
    modified = models.DateTimeField('Modificado', auto_now_add=True, editable=False, null=True, blank=True)
    modified_by = models.CharField('Modif. por', max_length=15, editable=False, null=True, blank=True)

    class Meta:
        # self._meta.app_label
        # self._meta.model_name
        abstract = True

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.created_by = get_current_user().username
        else:
            self.modified = datetime.now()
            self.modified_by = get_current_user().username
        super(CommonStruct, self).save(*args, **kwargs)

    def delete(self):
        self.active = False
        self.save()

    def hard_delete(self):
        super(CommonStruct, self).delete()

    def get_fields(self):
        """Devuelve una lista con los nombres de todos los campos"""
        fields = []
        for f in self._meta.fields:
            # comprobamos que el campo sea del tipo que queremos visualizar
            if f.editable and f.name not in ('id', 'active'):
                try:
                    value = getattr(self, f.name)
                    if value:
                        if f.choices:
                            fields.append({'name':f.verbose_name, 'value':dict(f.choices)[value],})
                        else:
                            fields.append({'name':f.verbose_name, 'value':value,})
                except:
                    value = None
        return fields

    def get_absolute_url(self):
        return reverse('%s:detail' % self._meta.model_name, args=(self.pk,))

    def get_list_url(self):
        return reverse('%s:list' % self._meta.model_name)

    def get_create_url(self):
        # self._meta.model_name
        # self._meta.module_name
        return reverse('%s:create' % self._meta.model_name)

    def get_detail_url(self):
        return reverse('%s:detail' % self._meta.model_name, args=(self.pk,))

    def get_update_url(self):
        # return reverse('%s:update' % self._meta.model_name, args=(self.pk,))
        # return reverse('%s:update' % self._meta.model_name, args=(self.pk,))
        return reverse('%s:update' % self._meta.model_name, args=(self.pk,))

    def get_delete_url(self):
        return reverse('%s:delete' % self._meta.model_name, args=(self.pk,))

    def get_app_label(self):
        return self._meta.model_name

    def get_module_name(self):
        return self._meta.module_name


class Pais(CommonStruct):
    nombre = models.CharField(max_length=40)
    cod_area_tel = models.CharField('Cód. Area Telef.', max_length=4, null=True, blank=True)

    class Meta:
        db_table = 'pais'
        verbose_name = 'País'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.nombre


class Provincia(CommonStruct):
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)

    # configuración para admin
    list_display = ['pais', 'nombre']
    list_display_links = ['nombre']
    list_filter = ['pais__nombre']
    search_fields = ['nombre']

    class Meta:
        db_table = 'provincia'
        ordering = ['nombre']
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'

    def __str__(self):
        return self.nombre


class Departamento(CommonStruct):
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)

    # configuración para admin
    list_display = ['provincia', 'nombre']
    list_display_links = ['nombre']
    list_filter = ['provincia__nombre']
    search_fields = ['nombre']

    class Meta:
        db_table = 'departamento'
        ordering = ['nombre']
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return self.nombre


class Localidad(CommonStruct):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150)
    cod_postal = models.CharField('Cód. Postal', max_length=12, null=True, blank=True)
    cod_area_tel = models.CharField('Cód. Area Telef.', max_length=4, null=True, blank=True)

    # configuración para admin
    list_display = ['id', 'nombre', 'cod_postal', 'cod_area_tel']
    list_display_links = ['nombre']
    exclude = []
    search_fields = ['nombre']
    list_filter = ['departamento']

    class Meta:
        db_table = 'localidad'
        ordering = ['nombre']
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'

    def __str__(self):
        return self.nombre


# class georef(CommonStruct):
#     NIVEL = (
#         ('01', 'País'),
#         ('02', 'Provincia'),
#         ('03', 'Departamento'),
#         ('04', 'Municipio'),
#         ('05', 'Localidad'),
#     )

#     nivel = models.CharField(max_length=2, choices=NIVEL, default='05')
#     nombre = models.CharField(max_length=60)
#     parent = models.ForeignKey('self', on_delete=models.CASCADE,
#                                null=True, blank=True, verbose_name='Padre')
#     georef_id = models.CharField(max_length=15, null=True, blank=True)
#     georef_nombre = models.CharField(max_length=100, null=True, blank=True)

#     # configuración para admin
#     list_display = ['parent', 'nivel', 'nombre', 'active']
#     list_display_links = ['nombre']
#     search_fields = ['nombre']
#     list_filter = ['parent']

#     class Meta:
#         verbose_name = 'GeoReferencia'
#         verbose_name_plural = 'GeoReferencias'

#     def __str__(self):
#         return self.nombre


class Diccionario(CommonStruct):
    TABLA = (
        ('comunicacion', 'Comunicaciones'),
        ('domicilio', 'Domicilios'),
        ('tipoEmpresa', 'Tipo de Empresa'),
    )

    texto = models.CharField(max_length=150)
    tabla = models.CharField(max_length=45, choices=TABLA, default='comunicacion')

    class Meta:
        db_table = 'diccionario'
        verbose_name = 'Diccionario'
        verbose_name_plural = 'Diccionarios'

    def __str__(self):
        # return "%s (%s)" % (self.texto, self.get_tabla_display())
        return self.texto

    def get_texto(self):
        return str(self.texto).capitalize()


# TODO:
# from smart_selects.db_fields import ChainedForeignKey
# localidad = ChainedForeignKey(Localidad,
#                                   chained_field="departamento",
#                                   chained_model_field="departamento",
#                                   show_all=False, auto_choose=True, sort=True,
#                                   null=True, blank=True)    

class Domicilio(CommonStruct):
    TIPO_CALLE = (('avda', 'Avenida'), ('barrio', 'Barrio'), ('calle', 'Calle'),
                  ('gps', 'Geo Posicionamiento'), ('pje', 'Pasaje'), ('ruta', 'Ruta'))

    tipo = models.ForeignKey(Diccionario, on_delete=models.CASCADE,
                             null=True, blank=True, default=1,
                             limit_choices_to={'tabla': 'domicilio', 'active': True})
    tipo_calle = models.CharField(max_length=6, choices=TIPO_CALLE, default='calle')
    nombre = models.CharField(max_length=80, null=True, blank=True)
    numero = models.IntegerField('Número', null=True, blank=True)
    piso = models.CharField(max_length=2, null=True, blank=True)
    puerta = models.CharField(max_length=2, null=True, blank=True)
    barrio = models.CharField(max_length=40, null=True, blank=True)
    # pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE,
                                  null=True, blank=True,
                                  limit_choices_to={'active': True})
    # departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE,
    #                                  null=True, blank=True,
    #                                  limit_choices_to={'active': True})
    # localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE,
    #                               null=True, blank=True,
    #                               limit_choices_to={'active': True})
    departamento = ChainedForeignKey(Departamento, 
                                     chained_field="provincia",
                                     chained_model_field="provincia",
                                     show_all=False, auto_choose=True, sort=True,
                                     null=True, blank=True)    
    localidad = ChainedForeignKey(Localidad,
                                  chained_field="departamento",
                                  chained_model_field="departamento",
                                  show_all=False, auto_choose=True, sort=True,
                                  null=True, blank=True)
    provincia_texto = models.CharField(max_length=50, null=True, blank=True)
    departamento_texto = models.CharField(max_length=50, null=True, blank=True)
    localidad_texto = models.CharField(max_length=50, null=True, blank=True)
    observacion_texto = models.TextField('Nota', null=True, blank=True)

    # configuración para admin
    date_hierarchy = ''
    exclude = []
    list_display = ['id', 'tipo', 'nombre', 'numero', 'piso', 'puerta', 'active']
    list_display_links = ['id']
    list_filter = ['provincia']
    ordering = ['tipo', 'nombre', 'numero']
    search_fields = ['nombre']

    class Meta:
        db_table = 'domicilio'
        verbose_name = 'Domicilio'
        verbose_name_plural = 'Domicilios'

    def __str__(self):
        texto = self.nombre
        if self.numero:
            texto += " " + str(self.numero)
        if self.piso:
            texto += " - %s piso, puerta %s" % (self.piso, self.puerta)
        return texto


class Comunicacion(CommonStruct):
    tipo = models.ForeignKey(Diccionario, on_delete=models.CASCADE,
                             null=True, blank=True, default=3,
                             limit_choices_to={'tabla': 'comunicacion', 'active': True})
    texto = models.CharField(max_length=150)

    # configuración para admin
    list_display = ['id', 'tipo', 'texto']
    list_display_links = ['id']
    exclude = []
    search_fields = []
    list_filter = []
    date_hierarchy = ''

    class Meta:
        db_table = 'comunicacion'
        verbose_name = 'Comunicación'
        verbose_name_plural = 'Comunicaciones'

    def __str__(self):
        return "%s: %s" % (self.tipo, self.texto)

    def get_comunicacion(self):
        return "{}: {}".format(self.get_tipo_display(), self.texto)
