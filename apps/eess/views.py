from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, transaction
from django.shortcuts import redirect, render, reverse
from django.utils.http import is_safe_url
from django.views import generic
from django.views.generic.base import RedirectView

from apps.comunes.functions import redirect_to, redirect_to_with_next, get_url_referer
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


class KioscoTemplateView(generic.TemplateView):
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
from cart.cart import Cart


# @login_required(login_url="/accounts/login/")
def cart_detail(request):
    return render(request, 'carrito/carrito.html', {'next': get_url_referer(request, 'eess:index')})


# @login_required(login_url='/accounts/login/')
def cart_add(request, id):
    cart = Cart(request)
    product = models.Cartilla.objects.get(id=id)
    cart.add(product=product)
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'cartilla/'))
    # return redirect("eess:cart_detail")
    return redirect_to(request, 'eess:cart_detail')


# @login_required(login_url="/accounts/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect_to(request, 'eess:cart_detail')


# @login_required(login_url="/accounts/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = models.Cartilla.objects.get(id=id)
    cart.add(product=product)
    return redirect_to_with_next(request, 'eess:cart_detail')


# @login_required(login_url="/accounts/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = models.Cartilla.objects.get(id=id)
    cart.decrement(product=product)
    return redirect_to_with_next(request, 'eess:cart_detail')


# @login_required(login_url="/accounts/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = models.Cartilla.objects.get(id=id)
    cart.remove(product)
    return redirect_to_with_next(request, 'eess:cart_detail')


# @login_required(login_url="/accounts/login/")
def cart_checkout(request):
    return render(request, 'carrito/carrito_confirmar.html', {'next': reverse('eess:index')})


# @login_required(login_url="/accounts/login/")
def cart_confirm(request):
    if request.method == 'POST':
        codigo = request.session.session_key
        identificador = request.POST['firstName']
        cart = Cart(request)

        with transaction.atomic():
            # creamos cabecera del pedido
            pedido = models.Pedido.create(codigo, identificador)
            pedido.items = len(cart.cart)
            pedido.total = total_carrito(cart.cart)
            pedido.save()
            # creamos detalle del pedido
            for key,value in cart.cart.items():
                item = models.PedidoItem.create(pedido, int(key), int(value['quantity']), float(value['price']))
                item.save()
            # borramos carrito de compra
            cart.clear()

    return redirect('eess:index')


def total_carrito(carrito):
    try:
        total = 0.0
        for key,value in carrito.items():
            total = total + (value['quantity'] * float(value['price']))
    except:
        total = 0.0
    return total




# -------------------------------------------------------------------
# URL's para los pedidos realizados
# -------------------------------------------------------------------

class PedidoTemplateView(generic.TemplateView):
    template_name = 'carrito/pedidos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = models.Pedido.objects.filter(active=True).order_by('created')
        context['object_list'] = object_list
        return context


def pedido_cerrar(request, id):
    pedido = models.Pedido.objects.get(id=id)
    pedido.active = False
    pedido.save()
    return redirect('eess:pedidos')


def pedido_borrar(request, id):
    pedido = models.Pedido.objects.get(id=id)
    pedido.anulado = True
    pedido.active = False
    pedido.save()
    return redirect('eess:pedidos')
