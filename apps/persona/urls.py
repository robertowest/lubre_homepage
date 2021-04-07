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

    path('ajax_abrir_comunicacion/', views.ajax_abrir_comunicacion, name='ajax_abrir_comunicacion'),
    path('ajax_asociar_comunicacion/', views.ajax_asociar_comunicacion, name='ajax_asociar_comunicacion'),

    path('<int:fk>/comunicacion/', views.CreateContactView.as_view(), name='associate_with_contact'),
    path('<int:fk>/domicilio/', views.CreateAddressView.as_view(), name='associate_with_address'),

    path('<int:pk>/contacto/<int:fk>/eliminar/', views.persona_contacto_eliminar, name='persona_contacto_eliminar'),
]
