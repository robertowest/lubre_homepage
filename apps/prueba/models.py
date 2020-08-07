from django.db import models


class Actividad(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)


class Empresa(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=60)


class EmpresaActividades(models.Model):
    id = models.IntegerField(primary_key=True)
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING)
    actividad = models.ForeignKey(Actividad, models.DO_NOTHING)
