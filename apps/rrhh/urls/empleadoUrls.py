from django.urls import path

from apps.rrhh.views import empleadoViews as views

app_name = "empleado"

urlpatterns = [
    path('', views.EmpleadoTemplateView.as_view(), name='index'),
    path('listado/', views.EmpleadosListView.as_view(), name='list'),
    path('crear/', views.EmpleadoCreateView.as_view(), name='create'),
    path('<int:pk>/', views.EmpleadoDetailView.as_view(), name='detail'),
    path('<int:pk>/modificar/', views.EmpleadoUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.EmpleadoDeleteView.as_view(), name='delete'),

    path('<int:pk>/datos/', views.TabDatosDetailView.as_view(), name='tab_datos'),
    path('<int:pk>/denuncias/', views.TabDenunciasListView.as_view(), name='tab_denuncias'),
    path('<int:pk>/activos/', views.TabActivosListView.as_view(), name='tab_activos'),
    path('<int:pk>/vacaciones/', views.TabVacacionesListView.as_view(), name='tab_vacaciones'),
]