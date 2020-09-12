from django.urls import path

from . import views

app_name = 'eess'

urlpatterns = [
    # cartilla ----------------------------------------------------------------
    path('cartilla/', views.CartillaTemplateView.as_view(), name='index'),
    path('cartilla/cafeteria/', views.CafeteriaTemplateView.as_view(), name='cafeteria'),
    path('cartilla/combos/', views.CombosTemplateView.as_view(), name='combos'),
    path('cartilla/kiosko/', views.KioskoTemplateView.as_view(), name='kiosko'),
]
