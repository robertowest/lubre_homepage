from django.db import models


class Clientes(models.Model):
    idcliente = models.IntegerField(primary_key=True)
    cuit = models.CharField(max_length=13, blank=True, null=True)

    # idactividad = models.ForeignKey(Actividades, models.DO_NOTHING, db_column='idactividad')
    idactividad = models.IntegerField()

    # idcalifica = models.ForeignKey(Califica, models.DO_NOTHING, db_column='idcalifica')
    idcalifica = models.IntegerField()

    # idestadocliente = models.ForeignKey('Estadocliente', models.DO_NOTHING, db_column='idestadocliente')
    idestadocliente = models.IntegerField()

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
