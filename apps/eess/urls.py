from django.urls import path

from . import views

app_name = 'eess'

urlpatterns = [
    # cartilla ----------------------------------------------------------------
    path('cartilla/', views.CartillaTemplateView.as_view(), name='index'),
    path('cartilla/cafeteria/', views.CafeteriaTemplateView.as_view(), name='cafeteria'),
    path('cartilla/combos/', views.CombosTemplateView.as_view(), name='combos'),
    path('cartilla/kiosco/', views.KioscoTemplateView.as_view(), name='kiosco'),

    # carrito -----------------------------------------------------------------
    path('carrito/detalle/', views.cart_detail, name='cart_detail'),
    path('carrito/limpiar/', views.cart_clear, name='cart_clear'),
    path('carrito/agregar/<int:id>/', views.cart_add, name='cart_add'),
    path('carrito/sumar_item/<int:id>/', views.item_increment, name='item_increment'),
    path('carrito/restar_item/<int:id>/', views.item_decrement, name='item_decrement'),
    path('carrito/quitar_item/<int:id>/', views.item_clear, name='item_clear'),
    path('carrito/verificar/', views.cart_checkout, name='cart_checkout'),
    # path('carrito/confirmar/', views.cart_confirm, name='cart_confirm'),
    path('carrito/confirmar/', views.cart_confirm_mp, name='cart_confirm_mp'),

    # pedidos -----------------------------------------------------------------
    path('pedidos/', views.PedidoTemplateView.as_view(), name='pedidos'),
    path('pedido/<int:id>/cerrar/', views.pedido_cerrar, name='pedido_cerrar'),
    path('pedido/<int:id>/borrar/', views.pedido_borrar, name='pedido_borrar'),

    # mercadopago -------------------------------------------------------------
    # path('pago_recibido/<int:id>/', views.PaidReceivedView.as_view(), name='payment_received'),
    path('pago_recibido/', views.PaidReceivedView.as_view(), name='payment_received'),
    path('pago_failure/', views.PaidFailureView.as_view(), name='payment_failure'),
    path('pago_pending/', views.PaidPendingView.as_view(), name='payment_pending'),
]
