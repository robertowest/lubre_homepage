from django.db import models
from smart_selects.db_fields import ChainedForeignKey


class Provincia(models.Model):
    nombre = models.CharField(max_length=40)


class Departamento(models.Model):
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)


class Localidad(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150)


class Direccion(models.Model):
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, null=True, blank=True)
    # departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True, blank=True)
    # localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE, null=True, blank=True)
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
