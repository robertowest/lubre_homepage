from django.urls import path

from apps.rrhh.views import denunciaViews as views

app_name = "denuncia"

urlpatterns = [
    path('', views.DenunciaTemplateView.as_view(), name='index'),
    path('listado/', views.DenunciasListView.as_view(), name='list'),
    path('<int:fk>/crear/', views.DenunciaCreateView.as_view(), name='create'),
    path('<int:pk>/', views.DenunciaDetailView.as_view(), name='detail'),
    path('<int:pk>/modificar/', views.DenunciaUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.DenunciaDeleteView.as_view(), name='delete'),
]