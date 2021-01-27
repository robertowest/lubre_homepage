from django.urls import path

from apps.rrhh.views import vacacionesViews as views

app_name = "vacaciones"

urlpatterns = [
    path('', views.VacacionesTemplateView.as_view(), name='index'),
    path('listado/', views.VacacionesListView.as_view(), name='list'),
    path('crear/', views.VacacionesCreateView.as_view(), name='create'),
    path('<int:pk>/', views.VacacionesDetailView.as_view(), name='detail'),
    path('<int:pk>/modificar/', views.VacacionesUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.VacacionesDeleteView.as_view(), name='delete'),
]