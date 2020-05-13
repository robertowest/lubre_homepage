from django.db import models

# Create your models here.
class Equivalencia(models.Model):
    TIPO = ((None, 'Sin definir'),
            (11, 'AGRO'),
            ( 1, 'AUTOMOTRIZ CARTER'),
            ( 2, 'AUTOMOTRIZ TRANSMISION'),
            ( 3, 'FERROCARRIL'),
            (10, 'GRASAS'),
            ( 4, 'INDUSTRIAL'),
            ( 5, 'MECANIZADO'),
            ( 6, 'MOTO'),
            ( 7, 'NAUTICA'),
            ( 8, 'NAVAL'),
            ( 9, 'REFRIGERANTES'),
           )

    MARCA = ((12, 'Agip'),
             ( 7, 'Castrol'),
             ( 9, 'Chevron'),
             ( 4, 'elf'),
             (13, 'Fuchs'),
             (14, 'Gulf'),
             (15, 'John Deere'),
             (11, 'Kluber'),
             ( 3, 'Mobil'),
             ( 6, 'Petrobras'),
             ( 8, 'Petronas/Selenia'),
             (16, 'Repsol'),
             ( 2, 'Shell'),
             (10, 'Texaco'),
             ( 5, 'Total'),
             ( 1, 'YPF'),
            )
    producto = models.CharField('Producto', max_length=160)
    marca = models.SmallIntegerField('Marca', choices=MARCA, default=None)
    tipo = models.SmallIntegerField('Tipo', choices=TIPO, default=None)
    parent = models.ForeignKey('Equivalencia', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['producto']

    def __str__(self):
        return self.producto

    @property
    def marca_banner(self):
        if self.marca == 8:
            return 'selenia'
        elif self.marca == 15:
            return 'jdeere'
        else:
            return self.get_marca_display().lower()
