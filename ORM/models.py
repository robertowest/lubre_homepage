from django.db import models


class Clientes(models.Model):
    idcliente = models.IntegerField(primary_key=True)
    cuit = models.CharField(max_length=13, blank=True, null=True)

    idactividad = models.IntegerField(blank=True, null=True)
    idcalifica = models.IntegerField(blank=True, null=True)
    idestadocliente = models.IntegerField(blank=True, null=True)

    idformacobro = models.IntegerField(blank=True, null=True)
    idlista = models.IntegerField(blank=True, null=True)
    idtipimun = models.CharField(max_length=1, blank=True, null=True)
    idtipodoc = models.IntegerField(blank=True, null=True)
    idtipoingbruto = models.CharField(max_length=1, blank=True, null=True)
    idtipoiva = models.CharField(max_length=1, blank=True, null=True)
    iva = models.CharField(max_length=1, blank=True, null=True)

    nombre = models.CharField(max_length=60, blank=True, null=True)
    fantasia = models.CharField(max_length=60, blank=True, null=True)
    direc_d = models.CharField(max_length=60, blank=True, null=True)
    telef_d = models.CharField(max_length=20, blank=True, null=True)
    email_d = models.CharField(max_length=90, blank=True, null=True)
    bloqueado = models.CharField(max_length=1, blank=True, null=True)
    idprovincias = models.CharField(max_length=15, blank=True, null=True)
    localidad = models.CharField(max_length=60, blank=True, null=True)
    direccion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'
