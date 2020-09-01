from django.urls import path
from . import views

app_name = 'equivalencia'   # en template: request.resolver_match.app_name

urlpatterns = [
    # path('', views.EquivalenciaForm.as_view(), name='form'),
    path('', views.Equivalencia, name='form'),
    path('<int:pk>/', views.EquivalenciaDetail.as_view(), name='detail'),

    path('cargar/productos/ajax/', views.cargar_productos_ajax, name='cargar_productos_ajax'),
]
