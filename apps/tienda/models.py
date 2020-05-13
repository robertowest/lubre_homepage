from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Unidad(models.Model):
    unidad_id = models.CharField(db_column='idunidad', primary_key=True, max_length=15)
    descripcion = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidades'


class Categoria(models.Model):
    categoria_id = models.IntegerField(db_column='iddivision', primary_key=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'division'
        ordering = ('descripcion', )
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'

    def __str__(self):
        return self.descripcion

    def get_absolute_url(self):
        return reverse('tienda:producto_por_categoria', args=[self.categoria_id])

    @property
    def slug(self):
        return slugify(self.descripcion)


class ProductoComercial(models.Model):
    producto_id = models.IntegerField(db_column='idstock', primary_key=True)
    descripcion = models.CharField(max_length=80, blank=True, null=True)
    detalle = models.BinaryField(blank=True, null=True)
    litros = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    unidad = models.ForeignKey(Unidad, models.DO_NOTHING, db_column='idunidad', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='iddivision', blank=True, null=True)
    precio = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    activo = models.SmallIntegerField(db_column='web', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock'
        ordering = ('descripcion', )
        verbose_name = 'producto comercial'
        verbose_name_plural = 'productos comerciales'

    def __str__(self):
        return self.descripcion

    def get_absolute_url(self):
        return reverse('tienda:producto_detalle', args=[self.producto_id])
