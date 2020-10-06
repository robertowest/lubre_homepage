from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from apps.comunes.models import Domicilio, CommonStruct, Comunicacion
from apps.persona.models import Persona


class Comercial(CommonStruct):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    domicilios = models.ManyToManyField(Domicilio, blank=True,
                                        related_name='comercial_domicilios',
                                        limit_choices_to={'active': True})
    comunicaciones = models.ManyToManyField(Comunicacion, blank=True,
                                            related_name='comercial_comunicaciones',
                                            limit_choices_to={'active': True})
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True,
                                   limit_choices_to={'is_active': True})

    list_display = ['persona_id', 'persona', 'usuario', 'active']
    list_display_links = ['persona']
    search_fields = ['persona__apellido']
    ordering = ['persona__apellido', 'persona__nombre']

    class Meta:
        db_table = 'comercial'
        verbose_name = 'Comercial'
        verbose_name_plural = 'Comerciales'

    def __str__(self):
        if self.persona.apellido is None:
            return "-"
        else:
            return "%s %s" % (self.persona.nombre, self.persona.apellido)

    def get_absolute_url(self):
        # reverse('persona:info', kwargs={'pk': self.pk})
        return reverse('comercial:detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('comercial:update', args=(self.pk,))

    def get_delete_url(self):
        return reverse('comercial:delete', args=(self.pk,))


class ComercialComunicaciones(models.Model):
    comercial = models.ForeignKey(Comercial, models.DO_NOTHING)
    comunicacion = models.ForeignKey(Comunicacion, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'comercial_comunicaciones'
        unique_together = (('comercial', 'comunicacion'),)


class ComercialDomicilios(models.Model):
    comercial = models.ForeignKey(Comercial, models.DO_NOTHING)
    domicilio = models.ForeignKey(Domicilio, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'comercial_domicilios'
        unique_together = (('comercial', 'domicilio'),)


class Actividad(CommonStruct):
    nombre = models.CharField('Actividad', max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               null=True, blank=True, verbose_name='Padre')

    # configuración para admin
    list_display = ['nombre']
    list_display_links = ['nombre']
    search_fields = ['nombre']
    ordering = ['nombre']

    class Meta:
        db_table = 'actividad'
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'

    def __str__(self):
        if self.parent:
            return '{0} ({1})'.format(self.nombre, self.parent.nombre)
        return self.nombre


class Empresa(CommonStruct):
    nombre = models.CharField('Nombre de Fantasía', max_length=60)
    razon_social = models.CharField('Razón Social', max_length=60, unique=True)
    cuit = models.CharField('CUIT/CUIL', max_length=13, unique=True, null=True, blank=True)
    # limit_choices_to={'active': True}
    comercial = models.ForeignKey(Comercial, on_delete=models.CASCADE, null=True, blank=True)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE, null=True, blank=True,
                                  verbose_name='Actividad principal')
    actividades = models.ManyToManyField(Actividad, blank=True,
                                         related_name='empresa_actividades',
                                         limit_choices_to={'parent__isnull': False, 'active': True})
    comunicaciones = models.ManyToManyField(Comunicacion, blank=True,
                                            related_name='empresa_comunicaciones')
    observacion = models.TextField(null=True, blank=True)
    referencia_id = models.IntegerField('Referencia Externa', null=True, blank=True, unique=True)
    origen = models.IntegerField(null=True, blank=True)
    planilla = models.IntegerField(null=True, blank=True)
    # marca el registro para impactar contra firebird
    impactar = models.BooleanField(default=False, null=False, blank=False)

    # configuración para admin
    list_display = ['razon_social', 'cuit', 'nombre', 'active']
    list_display_links = ['razon_social']
    exclude = []
    search_fields = ['razon_social']
    list_filter = ['comercial']
    date_hierarchy = ''

    class Meta:
        db_table = 'empresa'
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.razon_social

    def get_related_url_with_comunication(self):
        return reverse('%s:associate_with_comunication' % self._meta.model_name, args=(self.pk,))

    def get_related_url_with_address(self):
        return reverse('%s:associate_with_address' % self._meta.model_name, args=(self.pk,))

    def get_related_url_with_contact(self):
        return reverse('%s:associate_with_contact' % self._meta.model_name, args=(self.pk,))

    def get_related_url_with_actividad(self):
        return reverse('%s:associate_with_actividad' % self._meta.model_name, args=(self.pk,))


class EmpresaComunicaciones(models.Model):
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING)
    comunicacion = models.ForeignKey(Comunicacion, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'empresa_comunicaciones'
        unique_together = (('empresa', 'comunicacion'),)


class EmpresaActividades(models.Model):
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING)
    actividad = models.ForeignKey(Actividad, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'empresa_actividades'
        unique_together = (('empresa', 'actividad'),)


class EmpresaActividadContactos(models.Model):
    # Empresa-Contacto ahora depende de Empresa-Actividad-Contacto
    empresa_actividad = models.ForeignKey(EmpresaActividades, models.DO_NOTHING, 
                                          related_name='ea_contactos')
    persona = models.ForeignKey(Persona, models.DO_NOTHING)
    cargo = models.CharField('Puesto', max_length=50, null=True, blank=True, default='¿puesto?')

    class Meta:
        managed = True
        db_table = 'empresa_actividad_contactos'
        unique_together = (('empresa_actividad', 'persona'),)


class EmpresaActividadDomicilios(models.Model):
    # Empresa-Domicilio ahora depende de Empresa-Actividad-Domicilio
    empresa_actividad = models.ForeignKey(EmpresaActividades, models.DO_NOTHING, 
                                          related_name='ea_domicilios')
    domicilio = models.ForeignKey(Domicilio, models.DO_NOTHING)

    class Meta:
        managed = True  # False
        db_table = 'empresa_actividad_domicilios'
        unique_together = (('empresa_actividad', 'domicilio'),)


class EmpresaActividadInfo(CommonStruct):
    from apps.comunes.models import Diccionario

    TAMANO = ((1, 'Pequeña'), (2, 'Mediana'), (3, 'Grande'))

    # agro -------------
    empresa_actividad = models.ForeignKey(EmpresaActividades, on_delete=models.CASCADE, 
                                          related_name='ea_info')
    nombre = models.CharField('Nombre o identificación', max_length=150, null=True, blank=True)
    referencia_gps = models.CharField('Ubicación GPS', max_length=30, null=True, blank=True)
    superficie = models.SmallIntegerField('Hectareas', null=True, blank=True)
    # industria --------
    tamano = models.SmallIntegerField('Tamaño', choices=TAMANO, null=True, blank=True)
    tipo = models.ForeignKey(Diccionario, on_delete=models.CASCADE,
                             null=True, blank=True, verbose_name='Tipo de Empresa',
                             limit_choices_to={'tabla': 'tipoEmpresa', 'active': True})
    # agro: tipo de cultivos
    # industria: producto que fabrica
    comentario = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'empresa_actividad_info'


class Seguimiento(CommonStruct):
    TIPO = ((1, 'Visita'), (2, 'Llamada'), (3, 'Mensaje'))

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,
                                null=True, blank=True, limit_choices_to={'active': True})
    comercial = models.ForeignKey(Comercial, on_delete=models.CASCADE,
                                  null=True, blank=True, limit_choices_to={'active': True})
    fecha = models.DateField()
    tipo_calle = models.SmallIntegerField(choices=TIPO, default=1)
    mensaje = models.TextField(null=True, blank=True)
    respuesta = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'seguimiento'
        verbose_name = 'Seguimiento'
        verbose_name_plural = 'Seguimientos'
