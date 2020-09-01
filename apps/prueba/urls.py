from django.urls import path
from . import views

app_name = __package__.split('.')[1]    # en template: request.resolver_match.app_name

urlpatterns = [
    path('', views.index, name='index'),
    path('busqueda/', views.busqueda_modal, name='busqueda_modal'),
    path('busqueda2/', views.busqueda_table_modal, name='busqueda_table_modal'),

    # index y busqueda_modal son las requeridas


    path('ejemplo1/', views.comercial_search, name='comercial_search'),
    path('ejemplo2/', views.comercial_search_2.as_view(), name='comercial_search_2'),
    path('ejemplo3/', views.comercial_search_3, name='comercial_search_3'),

    # path('resultado/<int:pk>/', views.resultado.as_view(), name='resultado'),
    path('resultado/<int:pk>/', views.resultado, name='resultado'),


    path('prueba1/', views.companyListView, name="companyListView"),

    path('tabla/', views.tablaListView.as_view(), name="tablaListView"),

]
