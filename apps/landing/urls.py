from django.urls import path
from . import views

app_name = 'landing'   # en template: request.resolver_match.app_name

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('categoria/<int:pk>/', views.CategoriaListView.as_view(), name='categoria_list'),
    path('producto/<int:pk>/', views.ProductoDetail.as_view(), name='producto_detail'),
    path('servicio/<int:pk>/', views.ServicioDetail.as_view(), name='servicio_detail'),
]