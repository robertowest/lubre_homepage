from django.db import models

from apps.comunes.models import CommonStruct


def upload_product_path_handler(instance, filename):
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

    path = 'eess/cartilla'
    extension = '.' + filename.split('.')[1]
    file = str(new_id).zfill(5) + extension
    return '{dir}/{file}'.format(dir=path, file=file)


class Cartilla(CommonStruct):
    GRUPO = (
        ('avanzado', 'Combos Avanzado'),
        ('basico', 'Combos Básicos'),
        ('bebida', 'Bebidas'),
        ('cafe', 'Cafetería'),
        ('intermedio', 'Combos Intermedio'),
        ('kiosco', 'Kiosco'),
        ('promo', 'Promociones'),
        ('snak', 'Snaks'),
    )

    grupo = models.CharField(max_length=12, choices=GRUPO)
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion = models.CharField(max_length=150)
    imagen = models.FileField(upload_to=upload_product_path_handler, blank=True, null=True)

    # configuración para admin
    list_display = ['id', 'grupo', 'nombre', 'descripcion', 'precio', 'active']
    list_display_links = ['id']
    search_fields = ['nombre', 'descripcion']
    list_filter = ['grupo']

    class Meta:
        db_table = 'cartilla'
        verbose_name = 'Cartilla'
        verbose_name_plural = 'Cartillas'

    def __str__(self):
        return self.nombre
