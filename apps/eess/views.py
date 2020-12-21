from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db import IntegrityError, transaction
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.http import is_safe_url
from django.views import generic
from django.views.generic.base import RedirectView

from apps.comunes.functions import redirect_to, redirect_to_with_next, get_url_referer
from . import models


class PDFTemplateView(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        return CartillaTemplateView.as_view()(request)


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
    return render(request, 'carrito/carrito_confirmar_mp.html', {'next': reverse('eess:index')})


# @login_required(login_url="/accounts/login/")
def cart_confirm(request):
    if request.method == 'POST':
        codigo = request.session.session_key
        identificador = request.POST['firstName']
        cart = Cart(request)

        __mercadoPago(cart.cart)

        with transaction.atomic():
            # creamos cabecera del pedido
            pedido = models.Pedido.create(codigo, identificador)
            pedido.items = len(cart.cart)
            pedido.total = __total_carrito(cart.cart)
            pedido.save()
            # creamos detalle del pedido
            for key,value in cart.cart.items():
                item = models.PedidoItem.create(pedido, int(key), int(value['quantity']), float(value['price']))
                item.save()
            # borramos carrito de compra
            cart.clear()

    return redirect('eess:index')


def __total_carrito(carrito):
    try:
        total = 0.0
        for key,value in carrito.items():
            total = total + (value['quantity'] * float(value['price']))
    except:
        total = 0.0
    return total


import mercadopago
def __mercadoPago(carrito):
    mp = mercadopago.MP('TEST-1534881774722776-120914-533d8cfe4ab6b720548a020387446186-129446137')

    # user = request.user
    # articulo_orden = ArticuloOrden.objects.filter(usuario=user, finalizado=False)
    items=[]
    for key,value in carrito.items():
        datos = {
            'title': value['name'],
            'quantity': value['quantity'],
            'currency_id': 'ARS',
            'unit_price': float(value['price']),
        }
        items.append(datos)

    preference = {
        "items":items,
        "back_urls": [
            {
                "success": reverse('eess:payment_received')
            },
        ],
        "auto_return": "approved",
    }    

    preferenceResult = mp.create_preference(preference)
    url_forward = preferenceResult['response']['init_point']
    print(preferenceResult)
    return HttpResponseRedirect(url_forward)


# -------------------------------------------------------------------
# URL's para mercadopago
# -------------------------------------------------------------------

class PaidReceivedView(generic.TemplateView):
    # template_name = 'mercadoPago/paid_received.html'
    def get(self, request, *args, **kwargs):
        return render(request, 'mercadoPago/paid_received.html')


class PaidFailureView(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'mercadoPago/paid_failure.html')


class PaidPendingView(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'mercadoPago/paid_pending.html')


# -------------------------------------------------------------------
# URL's para los pedidos realizados
# -------------------------------------------------------------------

class PedidoTemplateView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'carrito/pedidos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = models.Pedido.objects.filter(active=True).order_by('created')
        context['object_list'] = object_list
        return context


@login_required(login_url="/accounts/login/")
def pedido_cerrar(request, id):
    pedido = models.Pedido.objects.get(id=id)
    pedido.active = False
    pedido.save()
    return redirect('eess:pedidos')


@login_required(login_url="/accounts/login/")
def pedido_borrar(request, id):
    pedido = models.Pedido.objects.get(id=id)
    pedido.anulado = True
    pedido.active = False
    pedido.save()
    return redirect('eess:pedidos')












# PROBANDO EL FUNCIONAMIENTO DE MERCADO PAGO (sandbox)

def cart_confirm_mp(request):
    # if request.method == 'POST':
    #     preference = {
    #         "items": [
    #             {
    #                 "title": "Título del art.",
    #                 "quantity": 1,
    #                 "currency_id": "ARS",  # Available currencies at: https://api.mercadopago.com/currencies
    #                 "unit_price": 1800
    #             }
    #         ],
    #         "payers": [
    #             {
    #                 "name": "Marcelo",
    #                 "surname": "Longobardi",
    #                 "email": "mlonog@correo.com",
    #                 "phone.number": "3816168252",
    #                 "identification": {
    #                     "type": "DNI",
    #                     "number": "12345678",
    #                 },
    #                 "address": {
    #                     "zip_code": "4107",
    #                     "street_name": "LA RIOJA",
    #                     "street_number": "150",
    #                 }
    #             },
    #         ],
    #     }

    cart = Cart(request)

    items = []
    for key, value in cart.cart.items():
        item = {
            "title": value['name'],
            "quantity": int(value['quantity']),
            "currency_id": "ARS",
            "unit_price": float(value['price'])
        }
        items.append(item)

    # access_token = "TEST-1534881774722776-120914-533d8cfe4ab6b720548a020387446186-129446137"
    # mp = mercadopago.MP(access_token)
    # preferenceresult = mp.create_preference(preference)
    # url = preferenceresult["response"]["init_point"]

    # SANDBOX
    mp = mercadopago.MP("TEST-7820321725229373-122610-f8c19c351611443dbc0d72e296501d3d-389742581")
    mp.sandbox_mode(True)
    # preference = {"items": items}
    preference = {
        "items": [
            {
                "title": "Articulo 1",
                "quantity": 1,
                "currency_id": "ARS",
                "unit_price": 12
            },
            {
                "title": "Articulo 2",
                "quantity": 2,
                "currency_id": "ARS",
                "unit_price": 10
            },
        ],
    }
    preferenceresult = mp.create_preference(preference)

    # back_urls
    preferenceresult['response']['back_urls']['success'] = reverse('eess:payment_received')
    preferenceresult['response']['back_urls']['failure'] = reverse('eess:payment_failure')
    preferenceresult['response']['back_urls']['pending'] = reverse('eess:payment_pending')
    
    url = preferenceresult["response"]["sandbox_init_point"]
    return redirect(url)
