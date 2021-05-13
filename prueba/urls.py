from django.urls import path

from . import views

app_name = 'prueba'

urlpatterns = [
    path('', views.DireccionCreateView.as_view(), name='create'),
    path('<int:pk>/', views.DireccionUpdateView.as_view(), name='update'),
]
