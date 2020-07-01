# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Clientes(models.Model):
    idcliente = models.IntegerField(primary_key=True)
    cuit = models.CharField(max_length=13, blank=True, null=True)
    # idactividad = models.ForeignKey(Actividades, models.DO_NOTHING, db_column='idactividad')
    # idcalifica = models.ForeignKey(Califica, models.DO_NOTHING, db_column='idcalifica')
    # idestadocliente = models.ForeignKey('Estadocliente', models.DO_NOTHING, db_column='idestadocliente')
    # idformacobro = models.ForeignKey('Formacobros', models.DO_NOTHING, db_column='idformacobro')
    # idtipoingbruto = models.ForeignKey('Tipoingbruto', models.DO_NOTHING, db_column='idtipoingbruto')
    # idlista = models.ForeignKey('Listas', models.DO_NOTHING, db_column='idlista')
    # idtipimun = models.ForeignKey('Tipimun', models.DO_NOTHING, db_column='idtipimun')
    # idtipoiva = models.ForeignKey('Tipoiva', models.DO_NOTHING, db_column='idtipoiva')
    # nombre = models.CharField(max_length=60, blank=True, null=True)
    # fantasia = models.CharField(max_length=60, blank=True, null=True)
    # iva = models.CharField(max_length=1, blank=True, null=True)
    # padron = models.CharField(max_length=10, blank=True, null=True)
    # canal = models.IntegerField(blank=True, null=True)
    # tipoope = models.CharField(max_length=1, blank=True, null=True)
    # credito = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    # maxsant = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    # morapant = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    # ctacte = models.IntegerField(blank=True, null=True)
    # directivos = models.CharField(max_length=60, blank=True, null=True)
    # direc_d = models.CharField(max_length=60, blank=True, null=True)
    # telef_d = models.CharField(max_length=20, blank=True, null=True)
    # email_d = models.CharField(max_length=90, blank=True, null=True)
    # codpro1 = models.CharField(max_length=15, blank=True, null=True)
    # comision = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    # fechaalta = models.DateTimeField(blank=True, null=True)
    # datospc = models.CharField(max_length=60, blank=True, null=True)
    # idopera = models.IntegerField(blank=True, null=True)
    # idplan = models.IntegerField(blank=True, null=True)
    # idplancanje = models.IntegerField(blank=True, null=True)
    # bloqueado = models.CharField(max_length=1, blank=True, null=True)
    # idclasifica = models.IntegerField(blank=True, null=True)
    # fechacalifica = models.DateField(blank=True, null=True)
    # idcli_nivel1 = models.IntegerField(blank=True, null=True)
    # idcli_nivel2 = models.IntegerField(blank=True, null=True)
    # idcli_nivel3 = models.IntegerField(blank=True, null=True)
    # idprocanje = models.IntegerField(blank=True, null=True)
    # idprovincias = models.CharField(max_length=15, blank=True, null=True)
    # localidad = models.CharField(max_length=60, blank=True, null=True)
    # direccion = models.CharField(max_length=60, blank=True, null=True)
    # idtipodoc = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'

