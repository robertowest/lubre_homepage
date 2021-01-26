from datetime import date, timedelta

from django.contrib.auth.models import User
from django.db.models import Q
from django.utils import timezone
from django.db import models
from django.urls import reverse_lazy

from apps.comunes.models import CommonStruct
# from apps.comunes.models import Domicilio, Comunicacion
from apps.persona.models import Persona


class Tarea(CommonStruct):
    descripcion = models.CharField(max_length=40, blank=False, null=False)

    class Meta:
        # app_label = 'rrhh'
        # db_table = 'tarea'
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering = ['descripcion']

    def __str__(self):
        return self.descripcion


def upload_employer(instance, filename):
    if not instance.id:
        Model = instance.__class__
        new_id=None
        try:
            new_id = Model.objects.order_by("id").last().id
            if new_id:
                new_id += 1
            else:
                pass
        except:
            new_id=1
    else:
        new_id = instance.id

    path = 'rrhh/empleado'
    extension = '.' + filename.split('.')[1]
    file = str(new_id).zfill(5) + extension
    return '{dir}/{file}'.format(dir=path, file=file)


class Empleado(CommonStruct):
    # definimos una propiedad que no será persistente
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._anio = date.today().year

    def get_anio(self):
        return self._anio

    def set_anio(self, value):
        self._anio = value
    # fin de la definimos no persistente

    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, primary_key=True)
    legajo = models.CharField(max_length=4, blank=False, null=False)
    fecha_ingreso = models.DateField('Fecha Ingreso', blank=True, null=True)
    fecha_egreso = models.DateField('Fecha Egreso',blank=True, null=True)
    imagen = models.FileField(upload_to=upload_employer, blank=True, null=True)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, blank=True, null=True,
                              limit_choices_to = {'active': True})
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True,
                                   limit_choices_to={'is_active': True})
    anio = property(get_anio, set_anio)

    list_display = ['persona_id', 'persona', 'usuario', 'active']
    list_display_links = ['persona']
    search_fields = ['persona__apellido']
    ordering = ['persona__apellido', 'persona__nombre']

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['persona__apellido', 'persona__nombre']

    def __str__(self):
        return "{}, {}".format(self.persona.apellido, self.persona.nombre)

    @property
    def vacaciones(self):
        # Tu derecho se encuentra regulado en el art. 150 de la LCT y establece que: el trabajador gozará de un período
        # mínimo y continuado de descanso anual remunerado por los siguientes plazos:
        #
        # a) De catorce (14) días corridos cuando la antigüedad en el empleo no exceda de cinco (5) años.
        # b) De veintiún (21) días corridos cuando siendo la antigüedad mayor de cinco (5) años no exceda de diez (10).
        # c) De veintiocho (28) días corridos cuando la antigüedad siendo mayor de diez (10) años no exceda de veinte (20).
        # d) De treinta y cinco (35) días corridos cuando la antigüedad exceda de veinte (20) años.
        #
        # Para determinar la extensión de las vacaciones atendiendo a la antigüedad en el empleo, se computará como tal
        # aquélla que tendría el trabajador al 31 de diciembre del año al que correspondan las mismas. Si tu antigüedad
        # es menor a un año, para tener derecho a gozar de los días de vacaciones (mencionados en el punto a), deberías
        # haber prestado servicios durante la mitad, como mínimo, de los días hábiles comprendidos en el año calendario
        # o aniversario respectivo. Si no llegas a esta cantidad de días trabajados te corresponde 1 día de vacaciones
        # por cada 20 días de trabajo efectivo.
        # x = date(date.today().year, 12, 31)
        x = date(self.get_anio(), 12, 31)

        total = 0
        habiles = 0
        aprobadas = 0
        pendientes = 0

        if (self.fecha_ingreso != None):
            trabajado = int((x - self.fecha_ingreso).days / 365)
            if trabajado >= 1 and trabajado < 5:
                total = 14
            elif trabajado >= 5 and trabajado < 10:
                total = 21
            elif trabajado >= 10 and trabajado < 20:
                total = 28
            elif trabajado >= 20:
                total = 35
            else:
                if self.fecha_ingreso.month < 7:
                    total = 14
                else:
                    total = int((x - self.fecha_ingreso).days / 30)

            habiles = int((total / 7) * 5)

        filtro = Q(empleado_id = self.persona.id) & Q(fec_inicio__year = self.get_anio()) & Q(active = True)
        solicitadas = Vacaciones.objects.filter(filtro)
        for vac in solicitadas:
            if vac.estado == 'A':
                aprobadas += vac.dias_habiles
            elif vac.estado == 'P':
                pendientes += vac.dias_habiles

        dic = {'totales': total,
               'habiles': habiles,
               'aprobadas': aprobadas,
               'pendientes': pendientes,
               'faltan': habiles - (aprobadas + pendientes)}
        return dic


class Diccionario_ART(models.Model):
    descripcion = models.CharField(max_length=80)
    diccionario = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Diccionario ART'
        verbose_name_plural = 'Diccionarios ART'

    def __str__(self):
        return self.descripcion


class Denuncia_ART(CommonStruct):
    ESTADO = [('P', 'Pendiente'), ('A', 'Aceptado'), ('R', 'Rechazado')]

    siniestro = models.IntegerField()
    empleado = models.ForeignKey(Empleado,
                                 on_delete=models.CASCADE, null=False,
                                 limit_choices_to = {'active': True})
    fec_siniestro = models.DateField('Fecha Siniestro', default=timezone.now, blank=True, null=True)
    fec_denuncia = models.DateField('Fecha Denuncia', default=timezone.now, blank=True, null=True)
    tipo_accidente = models.ForeignKey(Diccionario_ART, models.DO_NOTHING, null=True, blank=True,
                                       related_name='tipo_accidente_id',
                                       verbose_name='Tipo de Accidente',
                                       limit_choices_to = {'diccionario': 'tipoAccidente'})
    tipologia = models.ForeignKey(Diccionario_ART, models.DO_NOTHING, null=True, blank=True,
                                  related_name='tipologia_id',
                                  limit_choices_to = {'diccionario': 'tipologia'})
    zona_afectada = models.TextField('Zona Afectada', blank=True, null=True)
    estado = models.CharField(max_length=1, choices=ESTADO, default='P', blank=True, null=True)
    fec_alta_medica = models.DateField('Fecha Alta', blank=True, null=True)
    motivo_alta = models.ForeignKey(Diccionario_ART, models.DO_NOTHING, null=True, blank=True,
                                    related_name='motivo_alta_id',
                                    verbose_name='Motivo de Alta',
                                    limit_choices_to = {'diccionario': 'motivoAlta'})

    class Meta:
        verbose_name = 'Denuncia ART'
        verbose_name_plural = 'Denuncias ART'
        ordering = ['fec_siniestro']

    def __str__(self):
        return str(self.siniestro)

    @property
    def dias_perdidos(self):
        if self.fec_alta_medica is None:
            return (date.today() - self.fec_siniestro).days
        else:
            return (self.fec_alta_medica - self.fec_siniestro).days


class DiasVacaciones(CommonStruct):
    empleado = models.ForeignKey(Empleado,
                                 on_delete=models.CASCADE, null=False,
                                 limit_choices_to = {'active': True})
    periodo = models.SmallIntegerField('Año')
    dias_vacaciones = models.SmallIntegerField('Días de vacaciones')
    dias_disfrutados = models.SmallIntegerField('Días disfrutados')
    dias_pendientes = models.SmallIntegerField('Días pendientes')

    class Meta:
        verbose_name = 'Dia de Vacación'
        verbose_name_plural = 'Dias de Vacaciones'
        ordering = ['empleado', 'periodo']

    def __str__(self):
        return '{} ({})'.format(self.empleado, self.periodo)


class Vacaciones(CommonStruct):
    ESTADO = [('A', 'Aprobada'), ('P', 'Pendiente'), ('C', 'Cancelada')]

    empleado = models.ForeignKey(Empleado,
                                 on_delete=models.CASCADE, null=False,
                                 limit_choices_to = {'active': True})
    fecha_inicio = models.DateField('Fecha Inicio', blank=True, null=False)
    fecha_fin = models.DateField('Fecha Fin',blank=True, null=False)
    fecha_solicitud = models.DateField('Fecha Solicitud', blank=True, null=True)
    periodo = models.SmallIntegerField('Año', blank=True, null=True)
    observacion = models.TextField('Observación', blank=True, null=True)
    estado = models.CharField(max_length=1, choices=ESTADO, default='P', blank=True, null=False)

    class Meta:
        verbose_name = 'Vacaciones'
        verbose_name_plural = 'Vacaciones'
        ordering = ['empleado', 'periodo', 'fecha_inicio']

    def __str__(self):
        return '{} - {}'.format(self.fecha_inicio.strftime("%d/%m/%y"), self.fecha_fin.strftime("%d/%m/%y"))

    @property
    def dias_solicitados(self):
        return (self.fecha_fin - self.fecha_inicio).days + 1

    @property
    def dias_habiles(self):
        dias = 0
        for n in range(self.dias_solicitados):
            if (self.fecha_inicio + timedelta(n)).weekday() < 5:
                dias += 1
        return dias


class Feriados(CommonStruct):
    fecha = models.DateField(blank=False, null=False)
    descripcion = models.CharField('Descripción', max_length=60, blank=True, null=True)

    class Meta:
        verbose_name = 'Feriado'
        verbose_name_plural = 'Feriados'
        ordering = ['fecha']

    def __str__(self):
        return '{} ({})'.format(self.descripcion, self.fecha.strftime("%d/%m/%y"))


# -------------------------------------------------------------------
# Mantenimiento
#         +-----> Activo
#         +-----> Documentacion
#
# https://axiacore.com/blog/como-usar-genericforeignkey-en-django-554/
# -------------------------------------------------------------------


from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class Activo(CommonStruct):
    TIPO = [('D', 'Depósito'), ('V', 'Vehículo'), ('M', 'Material'), ('A', 'Documentación')]

    tipo = models.CharField(max_length=1, choices=TIPO, default='D')
    descripcion = models.CharField(max_length=40)
    responsable = models.ForeignKey(Empleado, models.DO_NOTHING, null=True, blank=True,
                                    limit_choices_to = {'active': True})

    class Meta:
        verbose_name = 'Activo'
        verbose_name_plural = 'Activos'
        ordering = ['tipo', 'descripcion']

    def __str__(self):
        return str(self.descripcion)


class Mantenimiento(CommonStruct):
    SEMAFORO = [(None, '---'), ('R', 'No Cumple'), ('A', 'Atención'), ('V', 'Cumple')]

    activo = models.ForeignKey(Activo, models.DO_NOTHING, null=True, blank=True,
                               related_name = 'mantenimientos',
                               limit_choices_to = {'active': True})
    descripcion = models.CharField('Descripción', max_length=60)
    estado = models.CharField(max_length=1, choices=SEMAFORO, default='V', blank=True, null=True)
    proximo = models.DateField('Próxima acción', default=timezone.now, blank=True, null=True)
    fecha_inicial = models.DateField('Fecha Inicial', default=timezone.now, blank=True, null=True)
    fecha_final = models.DateField('Fecha Final', default=timezone.now, blank=True, null=True)
    archivo = models.FileField(upload_to='rrhh/activos/', blank=True, null=True)

    class Meta:
        verbose_name = 'Mantenimiento'
        verbose_name_plural = 'Mantenimientos'

    def __str__(self):
        return str(self.descripcion)

    @property
    def dias_vencidos(self):
        if self.proximo is not None:
            return (date.today() - self.proximo).days
        if self.fecha_final is not None:
            return (date.today() - self.fecha_final).days
        return 0

    @property
    def archivo_url(self):
        if self.archivo and hasattr(self.archivo, 'url'):
            return self.archivo.url


# vista con activo-mantenimiento
class ActivoMantenimientoView(models.Model):
    id = models.IntegerField(primary_key=True)
    responsable = models.ForeignKey(Empleado, models.DO_NOTHING, null=True, blank=True,
                                    limit_choices_to = {'active': True})
    activo_id = models.IntegerField()
    tipo = models.CharField(max_length=1, choices=Activo.TIPO, default='D')
    activo = models.CharField(max_length=40)
    mantenimiento_id = models.IntegerField()
    mantenimiento = models.CharField(max_length=60, blank=True, null=True)
    estado = models.CharField(max_length=1, choices=Mantenimiento.SEMAFORO, default='V')
    proximo = models.DateField(blank=True, null=True)
    fecha_inicial = models.DateField('Válido desde', blank=True, null=True)
    fecha_final = models.DateField('Válido hasta', blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.activo, self.mantenimiento)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'rrhh.activo_mantenimiento_view'
