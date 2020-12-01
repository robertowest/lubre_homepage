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




# -------------------------------------------------------------------
# URL's para el carrito de compras
# -------------------------------------------------------------------

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from cart.cart import Cart


@login_required(login_url='/accounts/login/')
def cart_add(request, id):
    cart = Cart(request)
    product = models.Cartilla.objects.get(id=id)
    cart.add(product=product)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'cartilla/'))


@login_required(login_url="/accounts/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = models.Cartilla.objects.get(id=id)
    cart.remove(product)
    return redirect("eess:cart_detail")


@login_required(login_url="/accounts/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = models.Cartilla.objects.get(id=id)
    cart.add(product=product)
    return redirect("eess:cart_detail")


@login_required(login_url="/accounts/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = models.Cartilla.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("eess:cart_detail")


@login_required(login_url="/accounts/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("eess:cart_detail")


@login_required(login_url="/accounts/login/")
def cart_detail(request):
    return render(request, 'cartilla/carrito.html')
