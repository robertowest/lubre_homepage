from django.urls import path
from apps.empresa import views

app_name = 'empresa_actividad'

urlpatterns = [
    path('<int:pk>/', views.EmpActDetailView.as_view(), name='detail'),

    # crear registro en tablas asociadas
    path('<int:pk>/domicilio/', views.CreateAddressView.as_view(), name='emp_act_domicilio'),
    path('<int:pk>/contacto/', views.CreateContactView.as_view(), name='emp_act_contacto'),

    # asociar registro en tablas asociadas
    path('<int:pk>/contacto/buscar/', views.buscar_contacto, name='emp_act_contacto_buscar'),
    path('<int:relaId>/contacto/<int:conId>/', views.asociar_contacto, name='emp_act_contacto_asociar'),

    # re-asignar domicilio entre empresa-actividades
    path('<int:eaId>/ead/<int:eadId>/reasignar/', views.reasignar_domicilio, name='reasignar_domicilio'),
    path('<int:eaId>/reasignar/<int:eadId>/', views.reasignar_domicilio_ex, name='reasignar_ead'),

    # Empresa-Actividad-Domicilio
    path('eac/<int:eacId>/eliminar/', views.eac_delete, name='eac_delete'),
    path('ead/<int:eadId>/eliminar/', views.ead_delete, name='ead_delete'),
]
