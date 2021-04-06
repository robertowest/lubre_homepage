from django.urls import path

from . import views

app_name = 'prueba'

urlpatterns = [
    path('', views.ComunicacionTableView.as_view(), name='index'),
    path('filter_modal', views.comunicacion_table_view, name='filter_modal'),
]
