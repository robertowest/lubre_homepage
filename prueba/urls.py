from django.urls import path

from . import views

app_name = 'prueba'

urlpatterns = [
    path('<int:pk>/', views.PersonaDetailView.as_view(), name='detail'),

    path('ajax_cargar_filtro/', views.ajax_cargar_filtro, name='ajax_cargar_filtro'),
    path('ajax_cargar_tabla/', views.ajax_cargar_tabla, name='ajax_cargar_tabla'),
    path('ajax_asociar_elementos/', views.ajax_asociar_elementos, name='ajax_asociar_elementos'),
]
