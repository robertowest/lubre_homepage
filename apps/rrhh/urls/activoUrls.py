from django.urls import path

from apps.rrhh.views import activoViews as views

app_name = "activo"

urlpatterns = [
    path('', views.ActivoTemplateView.as_view(), name='index'),
    path('listado/', views.ActivosListView.as_view(), name='list'),
    path('<int:fk>/crear/', views.ActivoCreateView.as_view(), name='create'),
    path('<int:pk>/', views.ActivoDetailView.as_view(), name='detail'),
    path('<int:pk>/modificar/', views.ActivoUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.ActivoDeleteView.as_view(), name='delete'),
]