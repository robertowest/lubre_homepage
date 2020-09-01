from django.urls import path
from apps.empresa import views

app_name = 'comercial'  # en template: request.resolver_match.app_name

urlpatterns = [
    path('', views.ComercialTemplateView.as_view(), name='index'),
    path('listado/', views.ComercialListView.as_view(), name='list'),
    path('crear/', views.ComercialCreateView.as_view(), name='create'),
    path('<int:pk>/', views.ComercialDetailView.as_view(), name='detail'),
    path('<int:pk>/modificar/', views.ComercialUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.ComercialDeleteView.as_view(), name='delete'),
]
