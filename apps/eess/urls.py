from django.urls import path

from . import views

app_name = 'eess'

urlpatterns = [
    # cartilla ----------------------------------------------------------------
    path('cartilla/', views.CartillaTemplateView.as_view(), name='index'),
    path('cartilla/cafeteria/', views.CafeteriaTemplateView.as_view(), name='cafeteria'),
    path('cartilla/combos/', views.CombosTemplateView.as_view(), name='combos'),
    path('cartilla/kiosko/', views.KioskoTemplateView.as_view(), name='kiosko'),

    # carrito -----------------------------------------------------------------
    path('carrito/detalle/',views.cart_detail,name='cart_detail'),
    path('carrito/limpiar/', views.cart_clear, name='cart_clear'),
    path('carrito/agregar/<int:id>/', views.cart_add, name='cart_add'),
    path('carrito/sumar_item/<int:id>/', views.item_increment, name='item_increment'),
    path('carrito/restar_item/<int:id>/', views.item_decrement, name='item_decrement'),
    path('carrito/quitar_item/<int:id>/', views.item_clear, name='item_clear'),
    path('carrito/confirmar/', views.cart_checkout, name='cart_checkout'),
]
