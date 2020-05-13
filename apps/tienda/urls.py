from django.urls import include, path

from . import views

app_name = 'tienda'
urlpatterns = [
     path('', views.ProductoListView.as_view(), name='producto_listado'),
     # path('categoria/<int:categoria>/', views.ProductoListView.as_view(), name='producto_por_categoria'),
     # path('producto/<int:pk>/', views.ProductoDetailView.as_view(), name='producto_detalle'),
]
