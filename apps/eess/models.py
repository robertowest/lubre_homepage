from django.db import models
from datetime import datetime, timezone

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
    precio = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
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

    # propiedades para poder utilizar carrito de compra
    @property
    def name(self):
        return self.nombre

    @property
    def image(self):
        return self.imagen

    @property
    def price(self):
        return self.precio


class Pedido(CommonStruct):
    # user = models.ForeignKey(User, null=True, blank=True, on_delete='CASCADE')
    codigo = models.CharField(max_length=32)
    identificador = models.CharField(max_length=50)
    items = models.PositiveIntegerField(default=0)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    anulado = models.BooleanField(default=False)

    class Meta:
        db_table = 'cartilla_pedido'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        texto = "Pedido {}: {} artículos en preparación."
        return texto.format(self.codigo[0:5], self.items)

    @property
    def tiempo_transcurrido(self):
        td = datetime.now(self.created.tzinfo) - self.created
        return int((td.seconds // 60) % 60)  # minutos

    @classmethod
    def create(self, codigo, identificador):
        pedido = self(codigo=codigo, identificador=identificador)
        return pedido


class PedidoItem(CommonStruct):
    pedido = models.ForeignKey(Pedido, null=True, on_delete='CASCADE')
    producto = models.ForeignKey(Cartilla, null=True, on_delete='CASCADE')
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'cartilla_pedido_detalle'
        verbose_name = 'Detalle de pedido'
        verbose_name_plural = 'Detalle de pedidos'

    def __str__(self):
        return "{} - {} x ${} = ${}".format(self.producto.nombre, self.cantidad, self.producto.precio, self.cantidad * self.producto.precio)

    @classmethod
    def create(self, pedido, producto, cantidad, precio):
        cartilla = Cartilla.objects.get(id=producto)
        item = self(pedido=pedido, producto=cartilla, cantidad=cantidad, precio=cartilla.precio)
        return item
