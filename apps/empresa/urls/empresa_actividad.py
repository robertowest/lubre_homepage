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
    path('<int:empId>/contacto/<int:comId>/', views.asociar_contacto, name='emp_act_contacto_asociar'),
]
