from django import forms

from . import models

class EquivalenciaForm(forms.Form):
    producto = forms.CharField('Producto', max_length=160)
    marca = forms.SmallIntegerField('Marca', choices=models.Equivalencia.MARCA, default=None)
    tipo = forms.SmallIntegerField('Tipo', choices=models.Equivalencia.TIPO, default=None)
    parent = forms.ForeignKey('Equivalencia', on_delete=models.CASCADE, blank=True, null=True)