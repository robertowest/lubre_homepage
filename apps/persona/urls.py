from django.urls import path
from . import views

app_name = __package__.split('.')[1]    # en template: request.resolver_match.app_name

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.PersonaTemplateView.as_view(), name='index'),
    path('listado/', views.PersonasListView.as_view(), name='list'),
    path('crear/', views.PersonaCreateView.as_view(), name='create'),
    path('<int:pk>/', views.PersonaDetailView.as_view(), name='detail'),
    path('<int:pk>/modificar/', views.PersonaUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.PersonaDeleteView.as_view(), name='delete'),

    # modal para eliminación de registro
    path('<int:pk>/contacto/<int:fk>/eliminar/', views.persona_contacto_eliminar, name='persona_contacto_eliminar'),

    # modal para asociar elementos
    path('ajax_cargar_filtro/', views.ajax_cargar_filtro, name='ajax_cargar_filtro'),
    path('ajax_cargar_tabla/', views.ajax_cargar_tabla, name='ajax_cargar_tabla'),
    path('ajax_asociar_elementos/', views.ajax_asociar_elementos, name='ajax_asociar_elementos'),



    # TODO: comprobar si las entradastodavía son utilizadas
    path('<int:fk>/comunicacion/', views.CreateContactView.as_view(), name='associate_with_contact'),
    path('<int:fk>/domicilio/', views.CreateAddressView.as_view(), name='associate_with_address'),
]
