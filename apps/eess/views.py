from django.shortcuts import render
from django.views import generic

from . import models


# class PDFTemplateView(generic.TemplateView):
#     def get(self, request, *args, **kwargs):
#         return CartillaTemplateView.as_view()(request)


class CartillaTemplateView(generic.TemplateView):
    template_name = 'cartilla/index.html'


class CafeteriaTemplateView(generic.TemplateView):
    template_name = 'cartilla/recuadros.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = [
            models.Cartilla.objects.filter(grupo='cafe').filter(active=True).order_by('id')
        ]
        context['object_list'] = object_list
        return context


class CombosTemplateView(generic.TemplateView):
    model = models.Cartilla
    template_name = 'cartilla/recuadros.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = [
            models.Cartilla.objects.filter(grupo='basico').filter(active=True).order_by('id'),
            models.Cartilla.objects.filter(grupo='intermedio').filter(active=True).order_by('id'),
            models.Cartilla.objects.filter(grupo='avanzado').filter(active=True).order_by('id'),
        ]
        context['object_list'] = object_list
        return context


class KioskoTemplateView(generic.TemplateView):
    model = models.Cartilla
    template_name = 'cartilla/listado.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        promos = models.Cartilla.objects.filter(grupo='promo').filter(active=True).order_by('id')
        context['promos'] = promos
        object_list = [
            models.Cartilla.objects.filter(grupo='bebida').filter(active=True).order_by('id'),
            models.Cartilla.objects.filter(grupo='kiosco').filter(active=True).order_by('id'),
            models.Cartilla.objects.filter(grupo='snak').filter(active=True).order_by('id'),
        ]
        context['object_list'] = object_list
        return context
