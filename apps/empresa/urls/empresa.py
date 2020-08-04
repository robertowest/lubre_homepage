from django.urls import path
from apps.empresa import views

app_name = __package__.split('.')[1]

urlpatterns = [
    path('', views.EmpresaTemplateView.as_view(), name='index'),
    path('listado/', views.EmpresaListView.as_view(), name='list'),
    path('crear/', views.EmpresaCreateView.as_view(), name='create'),
    path('<int:pk>/', views.EmpresaDetailView.as_view(), name='detail'),
    path('<int:pk>/modificar/', views.EmpresaUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.EmpresaDeleteView.as_view(), name='delete'),

    # listado de empresas con filtro
    path('filtro_actividad/<int:filtro>', views.FilterListView.as_view(), name='filtro_actividad'),
    path('filtro_comercial/<int:filtro>', views.FilterListView.as_view(), name='filtro_comercial'),

    # alta de registros vinculados a la empresa
    path('<int:fk>/comunicacion/', views.CreateComunicationView.as_view(), name='associate_with_comunication'),
    path('<int:fk>/domicilio/', views.CreateAddressView.as_view(), name='associate_with_address'),
    path('<int:fk>/contacto/', views.CreateContactView.as_view(), name='associate_with_contact'),
    path('<int:fk>/actividad/', views.ActividadMultiListView.as_view(), name='associate_with_actividad'),

    # asociar con registro existente
    path('<int:pk>/comunicacion/buscar/', views.buscar_comunicacion, name='buscar_comunicacion'),
    path('<int:empId>/comunicacion/<int:comId>/', views.asociar_comunicacion, name='asociar_comunicacion'),

    path('<int:pk>/contacto/buscar/', views.buscar_contacto, name='buscar_contacto'),
    path('<int:empId>/contacto/<int:comId>/', views.asociar_contacto, name='asociar_contacto'),

    # redireccionamiento a empresa_actividad
    path('<int:empId>/actividad/<int:actId>/', views.empresa_actividad, name='empresa_actividad'),
]

# controlar login a nivel de path
# path('<int:pk>/recorrer/', login_required(views.EmpresaBrowseView.as_view()), name='browse'),

# ----------------------------------------------------------------------------------
# quitar despues de haber controlado todos los clientes por parte de los comerciales
# ----------------------------------------------------------------------------------
from django.contrib.auth.decorators import login_required

urlpatterns += [
    path('recorrer/', views.Recorrer, name="recorrer"),
    # path('recorrer/<int:comercial>/<int:empresa>/', 
    path('recorrer/<int:pk>/', 
         login_required(views.EmpresaBrowseView.as_view()), name="browse"),
]
