from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from ckeditor.fields import RichTextField

from apps.tienda.models import Categoria


def upload_path_handler(instance, filename):
    return '{dir}/{file}'.format(dir=instance.section.lower(), file=filename)

def upload_product_path_handler(instance, filename):
    path = 'product'
    extension = '.' + filename.split('.')[1]
    file = str(instance.id).zfill(5) + extension
    return '{dir}/{file}'.format(dir=path, file=file)


class Entries(models.Model):
    # SECTION = (('home', 'Inicio'), ('about', 'Acerca de'), ('service', 'Servicio'), ('team', 'Equipo'),
    #            ('work', 'Trabajo'), ('opinion', 'Testimonial'), ('pricing', 'Precios'),
    #            ('blog', 'Anuncios (blog)'), ('contact', 'Contacto'))

    SECTION = (('home', 'Inicio'),
               ('about', 'Acerca de'),
               ('whyus', 'Nosotros'),
               ('cataTag', 'Catalogo Tag'),
               ('catalog', 'Catalogo Items'),
               ('message', 'Testimonios'))

    section = models.CharField('Sección', max_length=15, choices=SECTION, default='home')
    label = models.CharField('Etiqueta', max_length=50)
    text_short = models.CharField('Texto breve', max_length=254, blank=True, null=True)
    # text_large = models.TextField('Texto largo', blank=True, null=True)
    text_large = RichTextField(verbose_name="Texto largo", blank=True, null=True)
    image = models.FileField(upload_to=upload_path_handler, blank=True, null=True)
    ordered = models.SmallIntegerField(verbose_name='Ordenación', default=1, blank=True, null=True)
    active = models.BooleanField('Activo', default=1, blank=True, null=True)

    class Meta:
        unique_together = ('section', 'label',)    # clave única
        verbose_name = "Entry"
        verbose_name_plural = "Entries"

    def __str__(self):
        
        return self.label.title()


class Category(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=128, blank=True)
    # content = models.TextField()
    content = RichTextField(blank=True, null=True)
    image = models.FileField(upload_to='blog/', blank=True, null=True)
    created_on = models.DateField(auto_now_add=True, blank=True)
    updated_on = models.DateField(auto_now=True, blank=True)
    publish_on = models.DateField(blank=True, null=True)

    list_display = ('title', 'category', 'author', 'publish_on','created_on','updated_on')
    search_fields = ['title']
    list_filter = ['category', 'tags', 'publish_on', 'created_on']
    date_hierarchy = 'pub_date'

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def publish(self):
        self.publish_on = timezone.now()
        self.save()

    # @property
    # def newer_post(self):
    #     if self.publish_on is not None:
    #         return next(iter(Post.objects.published().order_by("published").filter(published__gt=self.published)), None)
    @property
    def recent_post(self):
        qs = Post.objects.filter(publish_on__isnotnull=True)[:1]
        return next(iter(qs), None)


# agrupación de las categorías de productos
class Grupo(models.Model):
    nombre = models.CharField(max_length=25)
    # categoria = models.ForeignKey(Categoria, models.DO_NOTHING, blank=True, null=True)
    categoria = models.IntegerField(blank=True, null=True)
    activo = models.BooleanField(default=1, blank=True, null=True)

    class Meta:
        ordering = ('nombre', )
        verbose_name = 'grupo'
        verbose_name_plural = 'grupos'

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('tienda:producto_por_categoria', args=[self.categoria_id])


# definición de los productos sin presentación comercial
class Producto(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    # descripcion = models.TextField(blank=True, null=True)
    descripcion = RichTextField(verbose_name="Descripción", blank=True, null=True)
    grupo = models.ForeignKey(Grupo, models.DO_NOTHING, blank=True, null=True)
    imagen = models.FileField(upload_to=upload_product_path_handler, blank=True, null=True)
    ficha_tecnica = models.CharField('Ficha técnica', max_length=254, blank=True, null=True)
    ficha_seguridad = models.CharField('Ficha de seguridad', max_length=254, blank=True, null=True)
    activo = models.BooleanField('Activo', default=1, blank=True, null=True)

    class Meta:
        ordering = ('grupo', 'nombre', )
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('tienda:producto_detalle', args=[self.id])

    # para campos de tipo bytea -- descripcion = models.BinaryField(blank=True, null=True)
    # @property
    # def descripcion_texto(self):
    #     return bytes(self.descripcion).decode()


class Mensaje(models.Model):
    nombre = models.CharField(max_length=40, blank=False, null=False)
    correo = models.EmailField(max_length=100, blank=False, null=False)
    asunto = models.CharField(max_length=60, blank=False, null=False)
    mensaje = models.CharField(max_length=254, blank=False, null=False)
    leido = models.BooleanField('Leído', default=0, blank=True, null=True)
    creado = models.DateField(auto_now_add=True, blank=True)
    modificado = models.DateField(auto_now=True, blank=True)

    class Meta:
        verbose_name = 'mensaje'
        verbose_name_plural = 'mensajes'

    def __str__(self):
        return self.nombre
